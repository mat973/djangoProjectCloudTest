from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.ShowTuskView.as_view(),  name="tusk"),
    path('add/', views.AddTuskView.as_view(), name="tusk-add"),
    path('variable/<int:pk>', views.ShowVarableView.as_view(), name="tusk-variable"),
    path('submit_answer', views.form, name="submit_answer"),
    path('show/', views.ShowTuskAdminView.as_view(), name="show"),
]