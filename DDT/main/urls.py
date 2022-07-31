from django.urls import path
from .views import home, Login, Logout, profile, \
    borrowers, LenderList,CreateLender, lenderDetails, \
    borrowers_details, Register, CreateBorrower
urlpatterns = [
    path('', home),
    path('login/', Login),
    path('logout/', Logout),
    path('profile/', profile),
    path('borrowers/',borrowers.as_view()),
    path('lenders/', LenderList.as_view()),
    path('create_lender/', CreateLender),
    path('loan_details/<int:id>', lenderDetails, name='lender_details'),
    path('loan_details/<int:id>', borrowers_details, name='borrowers_details'),
    path('register/', Register),
    path('borrowering/', CreateBorrower)
]
