from django.urls import path
from .views import StateList, StateDetail

urlpatterns = [
    path('', StateList.as_view(), name='state_list'),
    path('<int:pk>', StateDetail.as_view(), name='state-detail'),
]