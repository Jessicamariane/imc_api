from django.contrib import admin
from django.urls import path
from core import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', api.PeopleList.as_view(), name="people-list"),
    path('people/<int:pk>/', api.PeopleDetail.as_view(), name="people-detail"),
]
