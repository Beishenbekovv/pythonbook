from django.urls import path
from students.views import *

app_name = 'students'

urlpatterns = [
    path('detail/<int:pk>/', StudentDetailAPIView.as_view(), name="students-detail"),
]
