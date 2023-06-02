from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
router = routers.DefaultRouter()
router.register(r'posts',views.PostViewSet, basename = "posts")



urlpatterns = [

    path('',include(router.urls)),
    # path('user/',views.UserList.as_view(),name="userList"),
    # path('user/<int:pk>',views.UserDetail.as_view(),name="userDetail"),
]
