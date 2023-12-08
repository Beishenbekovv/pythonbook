from django.urls import path, include
from students.views import *
from students.serializers import *

app_name = "student"

urlpatterns = [
    path('detail/<int:pk>/', StudentDetailAPIView.as_view(), name="student-detail"),
    path('list/', StudentsView.as_view(), name="list"),
]