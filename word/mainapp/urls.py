from django.urls import path
from .views import *

urlpatterns = [
    path('home_page/', home_page),
    path('4000_essential_english_words/', essential_english_words),

    path('query_essential_1/', query_essential_1),
    path('test_1_essential/', test_1_essential),

]
