from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('addItem/', views.add, name='add'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('filter_by_date/', views.filterByDate, name='filter')
]
