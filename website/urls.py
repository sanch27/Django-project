from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

    path('course/<int:pk>', views.customer_course, name='course'),
    path('delete_course/<int:pk>', views.delete_course, name='delete_course'),
    path('add_course/', views.add_course, name='add_course'),
    path('update_course/<int:pk>', views.update_course, name='update_course'),

    path('package/<int:pk>', views.customer_package, name='package'),
    path('delete_package/<int:pk>', views.delete_package, name='delete_package'),
    path('add_package/', views.add_package, name='add_package'),
    path('update_package/<int:pk>', views.update_package, name='update_package'),
]