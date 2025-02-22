from django.urls import path

from . import views

urlpatterns = [
    path("list", views.listUsers, name="listUsers"),
    path("create", views.createUserView, name="createUserView"),
    path("createUser", views.createUser, name="createUser"),
    path("details-user-id/<int:id>", views.userDetail, name="userDetail"),
    path("createUser-by-fetch",views.createUserByFetch, name="createUser-by-fetch")

]