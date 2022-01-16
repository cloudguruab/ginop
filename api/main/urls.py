from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('chain/', views.PrivateChainView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)