from django.urls import path
from . import views


urlpatterns = [
    path('register/' , views.register  , name='register'),
    path('user/info/' , views.current_user  , name='current_user'),
    path('user/update/' , views.update_profile  , name='user.profile.update'),
    path('forgot_password/' , views.forgot_password  , name='forgot_password'),
    path('reset_password/' , views.reset_password  , name='reset_password'),
]
