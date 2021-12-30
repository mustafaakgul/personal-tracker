from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = "accounts"


urlpatterns = [
    path("login/", views.login_view, name = "authentication"),
    path("registration/", views.registration_view, name="registration"),
    path("logout/", views.logout_view, name = "logoutAccount"),

    path("account-settings/<int:id>", views.settings, name="accountSettings"),
    path("account-settings-general/<int:id>", views.settingsGeneral, name="settingsGeneral"),
    path("test/<int:id>", views.test, name="test"),

    #path("hesaplar/", views.accountList, name="accountList"),

    path("password-change/<int:id>", views.changePassword, name="changePassword"),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]