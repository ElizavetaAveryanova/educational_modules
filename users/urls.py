from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import (UserRegisterView, UserListView, UserLoginView, UserProfileUpdateView, \
                         UserDeleteView,
                         UserPasswordResetView, UserPasswordResetConfirmView, confirm_registration, UserProfileView)

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='modules:index'), name='logout'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/<str:token>/', confirm_registration, name='confirmation_link'),  # Ваш путь для подтверждения
    path('confirm-registration/<uuid:token>/', confirm_registration, name='confirm_registration'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),  # URL для просмотра профиля
]
