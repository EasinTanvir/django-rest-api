from django.urls import path
from . import views


urlpatterns = [
    path("users/",views.CreateUser.as_view(),name="user-view-create"),
    path("users/<int:pk>/",views.UserUpdateDestroy.as_view(),name="user-update"),
]
