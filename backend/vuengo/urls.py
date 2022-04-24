from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from api.views import *
router = routers.DefaultRouter()



router.register(r'users', UserViewSet)
router.register(r'loanTermCustomer', LoanTermCustomerViewSet)
router.register(r'loanCustomer', LoanCustomerViewSet)
router.register(r'loanTermProvider', LoanTermProviderViewSet)
router.register(r'loanProvider', LoanProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('signIn/', signIn),
    path('signUp/', signUp),
    
    # Customer & Provider
    
    path('getLoanTerm/', getLoanTerm),
    path('requestLoan/', requestLoan),
    path('getPendingLoan/<int:id>/<int:check>', getPendingLoan),
    path('getActiveLoan/<int:id>/<int:check>', getPendingLoan),
    path('cancelLoan/', cancelLoan),
    path('makePayment/', makePayment),
    
    # Bank
    path('createLoanTerm/', createLoanTerm),
    path('approveDeclineLoan/', approveDeclineLoan),
    path('getBankStats/', bankStats),
]
