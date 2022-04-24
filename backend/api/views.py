from asyncio.windows_events import NULL
from django.shortcuts import render, redirect 
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import authenticate, login, logout

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.contrib import messages
import json
from django.db.models import Sum

from django.http import JsonResponse

import bcrypt
from django.contrib.auth.backends import BaseBackend

#  MODELS
from .models import *

#  SERIALIZERS
from .serializers import *

@api_view(['POST'])        
@csrf_exempt 
def signIn(request):  
    my_json = request.body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    
    username = data['username']
    password = data['password']
     
    try:
        userFound = User.objects.get(username=username)
        if userFound is not None:
            hashed_password = userFound.password
            is_check = bcrypt.checkpw(password.encode('utf8'),hashed_password.encode('utf8'))
    
            if is_check:
                return JsonResponse({"statusCode": 200,"status":"success","user":{'id':userFound.id,'username':userFound.username,'type':userFound.type}})
            else:
                return JsonResponse({"statusCode": 401,"status":"fail","message":'incorrect password'})
        else:
            return JsonResponse({"statusCode": 401,"status":"fail","message":'user not registered'})
    except:
        return JsonResponse({"statusCode": 400,"status":"fail","message":'user not registered'})


@api_view(['POST'])        
@csrf_exempt 
def signUp(request):  
    my_json = request.body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)

    username = data['username']
    password = data['password']
    password=str(bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt()),'utf-8')
    type = data['type']
    newUser={"username":username,"password":password,"type":type}
    
    try:
        userFound = User.objects.filter(username=username)
        if userFound:
            return JsonResponse({"statusCode": 401,"status":"fail","message":'username is taken'})
        else:
            serializer = UserSerializer(data=newUser)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"statusCode": 200,"status":"success","message":'user registered successfully',"user":{'username':username,'type':data['type']}})

    except:    
        return JsonResponse({"statusCode": 400,"status":"fail","message":'error'})

@api_view(['POST','PUT'])        
@csrf_exempt 
def requestLoan(request):
    try:
        serializer=None
        if request.method == 'POST':
            serializer = LoanCustomerSerializer(data=request.data)
            
        if request.method == 'PUT':    
            serializer = LoanProviderSerializer(data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"statusCode": 200,"status":"success"})
        else:
            return JsonResponse({"statusCode": 400,"status":"fail","message":'creation was not successful'})

    except:    
        return JsonResponse({"statusCode": 400,"status":"fail","message":'error'})

@api_view(['GET','POST'])        
@csrf_exempt 
def getLoanTerm(request):
    if request.method == 'GET':
        loanterms = LoanTermCustomer.objects.all()
        serializer = LoanTermCustomerSerializer(loanterms, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        loanterms = LoanTermProvider.objects.all()
        serializer = LoanTermProviderSerializer(loanterms, many=True)
        return Response(serializer.data)

@api_view(['POST','PUT'])        
@csrf_exempt 
def createLoanTerm(request):
    my_json = request.body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)    
    name = data['name']

    try:
        
        termFound=None
        if request.method == 'POST':
            termFound = LoanTermCustomer.objects.filter(name=name)
            
        if request.method == 'PUT':    
            termFound = LoanTermProvider.objects.filter(name=name)

        if termFound:
            return JsonResponse({"statusCode": 401,"status":"fail","message":'Loan name already exists'})
        else:
            
            serializer=None

            if request.method == 'POST':
                serializer = LoanTermCustomerSerializer(data=request.data)
            
            if request.method == 'PUT':    
                serializer = LoanTermProviderSerializer(data=request.data)
                
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"statusCode": 200,"status":"success"})
            else:
                return JsonResponse({"statusCode": 400,"status":"fail","message":'creation was not successful'})

    except:    
        return JsonResponse({"statusCode": 400,"status":"fail","message":'error'})
    
@api_view(['GET','POST'])        
@csrf_exempt 
def getPendingLoan(request, id,check):
    
    if id==0:
        if request.method == 'GET':
            loans = LoanCustomer.objects.filter(accepted=check)
            serializer = LoanCustomerSerializer(loans, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            loans = LoanProvider.objects.filter(accepted=check)
            serializer = LoanProviderSerializer(loans, many=True)
            return Response(serializer.data)
    else:    
        if request.method == 'GET':
            loans = LoanCustomer.objects.filter(user_id=id,accepted=check)
            serializer = LoanCustomerSerializer(loans, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            loans = LoanProvider.objects.filter(user_id=id,accepted=check)
            serializer = LoanProviderSerializer(loans, many=True)
            return Response(serializer.data)


@api_view(['DELETE','POST'])        
@csrf_exempt 
def cancelLoan(request):   
    my_json = request.body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    num = data['loanNum']
    try:
        if request.method == 'DELETE':
            LoanCustomer.objects.filter(id=num).delete()
        
        if request.method == 'POST':
            LoanProvider.objects.filter(id=num).delete()
            
        return JsonResponse({"statusCode": 200,"status":"success"})
    except:
        return JsonResponse({"statusCode": 400,"status":"fail"})
        
@api_view(['POST','PUT'])        
@csrf_exempt 
def approveDeclineLoan(request):
    my_json = request.body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    status = data['status']
    num = data['loanNum']
    try:
        if request.method == 'POST':
            if status==False:
                LoanCustomer.objects.filter(id=num).delete()
            else:
                t = LoanCustomer.objects.get(id=num)
                t.accepted = True 
                t.save() 
                                
        
        if request.method == 'PUT':
            if status==False:
                LoanProvider.objects.filter(id=num).delete()
            else:
                t = LoanProvider.objects.get(id=num)
                t.accepted = True 
                t.save() 
        
            
        return JsonResponse({"statusCode": 200,"status":"success"})
    except:
        return JsonResponse({"statusCode": 400,"status":"fail"})

@api_view(['POST','PUT'])        
@csrf_exempt 
def makePayment(request):
    my_json = request.body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    value = data['value']
    value=int(value)
    num = data['loanNum']
    try:
        t=None
        if request.method == 'POST':
            t = LoanCustomer.objects.get(id=num)
        else:
            t = LoanProvider.objects.get(id=num)
            
        if(t.paid+value<=t.value):
            t.paid += value
            t.save()
        else:
            return JsonResponse({"statusCode": 200,"status":"fail","message":"Unsuccessful: paid value is more than loan value"})
        
        if request.method == 'POST':
            t = LoanCustomer.objects.get(id=num)
        else:
            t = LoanProvider.objects.get(id=num)
            
        if(t.paid>=t.value):
            if request.method == 'PUT':
                LoanProvider.objects.filter(id=num).delete()
            else:
                LoanCustomer.objects.filter(id=num).delete()
                
            return JsonResponse({"statusCode": 200,"status":"success","message":"Loan was cleared and paid in full"})
        else:
            return JsonResponse({"statusCode": 200,"status":"success"})
        
    except:
        return JsonResponse({"statusCode": 400,"status":"fail","message":"error"})
    
@api_view(['GET'])        
@csrf_exempt 
def bankStats(request):
    try:
        sumValCust = LoanCustomer.objects.filter(accepted=True).aggregate(Sum('value'))['value__sum']
        sumValProv = LoanProvider.objects.filter(accepted=True).aggregate(Sum('value'))['value__sum']
        paidValCust = LoanCustomer.objects.filter(accepted=True).aggregate(Sum('paid'))['paid__sum']
        paidValProv = LoanProvider.objects.filter(accepted=True).aggregate(Sum('paid'))['paid__sum']
        
        return JsonResponse({"statusCode": 200,"status":"success","sumValCust":sumValCust,"sumValProv":sumValProv,"paidValCust":paidValCust,"paidValProv":paidValProv})
    except:
        return JsonResponse({"statusCode": 400,"status":"fail","message":"error"})
    

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
           
class LoanCustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LoanCustomer.objects.all()
    serializer_class = LoanCustomerSerializer
    
class LoanTermCustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LoanTermCustomer.objects.all()
    serializer_class = LoanTermCustomerSerializer
    
class LoanProviderViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LoanProvider.objects.all()
    serializer_class = LoanProviderSerializer
    
class LoanTermProviderViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LoanTermProvider.objects.all()
    serializer_class = LoanTermProviderSerializer