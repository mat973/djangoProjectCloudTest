from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.ShowNewsView.as_view(), name="home"),
    path('news/<int:pk>', views.NewDetailView.as_view(), name="news-detail"),
    path('news/add', views.CreateNewView.as_view(), name="new-add"),
    path('contacti', views.contakti,name="contakti")

]