from django.urls import path
from .views import villainsList, VillainDetail

urlpatterns = [
path('',villainsList.as_view(), name='villains_list'),
path('/<int:pk>/', VillainDetail.as_view(), name='villain_detail' )

]
