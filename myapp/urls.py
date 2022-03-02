from django.urls import path
from . import views
urlpatterns = [
    path('/',views.wellcome),
    path('group/',views.GroupView.as_view()),
    path('group/<str:pk>/',views.GroupView.as_view()),
    path('Assessable_value/',views.Assessable_valueView.as_view()),
    path('Assessable_value/<str:pk>/',views.Assessable_valueView.as_view()),
    path('ItemView/<str:pk>/',views.ItemView.as_view()),
    path('ItemView/',views.ItemView.as_view()),
    path('ProductView/<str:pk>/',views.ProductView.as_view()),
    path('ProductView/',views.ProductView.as_view()),
    path('CustomerView/<str:pk>/',views.CustomerView.as_view()),
    path('CustomerView/',views.CustomerView.as_view()),
    path('CityView/<str:pk>/',views.CityView.as_view()),
    path('CityView/',views.CityView.as_view()),
    path('CountryView/<str:pk>/',views.CountryView.as_view()),
    path('CountryView/',views.CountryView.as_view()),
    path('CountryView/<str:pk>/',views.CountryView.as_view()),
    path('CountryView/',views.CountryView.as_view()),
    path('TaxView/<str:pk>/',views.TaxView.as_view()),
    path('TaxView/',views.TaxView.as_view()),
#    path('login/',views.Loginview.as_view()),

]