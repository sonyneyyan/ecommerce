from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, UserDashboard, UserEditProfile, ChangePassword

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),  # User registration
    path('login/', UserLogin.as_view(), name='login'),          # User login
    path('logout/', UserLogout.as_view(), name='logout'),       # User logout
    path('dashboard/', UserDashboard.as_view(), name='dashboard'),  # User profile dashboard
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),  # Edit user profile
    path('change_password/', ChangePassword.as_view(), name='change_password'),  # Change password
]
