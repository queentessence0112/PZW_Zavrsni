from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginView ,name='login'),
    path('<int:id>/', views.pacijent_form,name='pacijent_update'),
    path('delete/<int:id>/',views.pacijent_delete,name='pacijent_delete'),
    path('form/', views.pacijent_form, name='pacijent_insert'),
    path('list/', views.pacijent_list, name='pacijent_list')
]
