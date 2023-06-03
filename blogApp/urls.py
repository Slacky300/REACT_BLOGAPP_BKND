from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
router = routers.DefaultRouter()
router.register(r'posts',views.PostViewSet, basename = "posts")
# router.register(r'comments/<slug:slug>/',views.CommentViewSet, basename = "comments")




urlpatterns = [

    path('',include(router.urls)),
    path('comments/<slug:slug>/',views.CommentViewSet.as_view(),name="commentList"),
    path('detcomments/<int:pk>/',views.CommentDetail.as_view(),name="cmntDetail")
    # path('comments/<int:pk>/',views.CommentDetailView.as_view(),name="commenDetail"),
    # path('getcomment/<slug:slug>/',views.getComments,name="getComments"),

]
