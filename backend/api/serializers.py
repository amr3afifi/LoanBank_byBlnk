from rest_framework import serializers
from .models import *


        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password','type')
        
class LoanTermCustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanTermCustomer
        fields = ('id', 'name','min','max','duration','interest')
        
class LoanCustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanCustomer
        fields = ('id', 'name','value','paid','accepted','start_date','term_id','user_id')
        
class LoanTermProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanTermProvider
        fields = ('id', 'name','min','max','duration','interest')
        
class LoanProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanProvider
        fields = ('id', 'name','value','paid','accepted','start_date','term_id','user_id')