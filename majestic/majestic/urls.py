from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('services/vyshivka-na-kroe', views.vyshivka_na_kroe, name='vyshivka-na-kroe'),
    path('services/shevrony-i-nashivki', views.shevrony_i_nashivki, name='shevrony-i-nashivki'),
    path('services/vyshivka-na-gotovyh-izdeliyah', views.vyshivka_na_gotovyh_izdeliyah,
            name='vyshivka-na-gotovyh-izdeliyah'),
    path('services/cerkovnaya-vyshivka', views.cerkovnaya_vyshivka, name='cerkovnaya-vyshivka'),
    path('cost/', views.cost, name='cost'),
    path('contacts/', views.contacts, name='contacts'),
]