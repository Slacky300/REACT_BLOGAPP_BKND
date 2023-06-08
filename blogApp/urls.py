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
    path('getlatesposts/',views.GetLatestPost.as_view(), name="get_lates_post"),
    path('comments/<slug:slug>/',views.CommentViewSet.as_view(),name="commentList"),
    path('detcomments/<int:pk>/',views.CommentDetail.as_view(),name="cmntDetail"),
    path("postcomments/<slug:slug>/",views.AddComment.as_view(),name="addcomment"),
    path('get_category/',views.GetCategory.as_view(),name="get_category"),
    # path('comments/<int:pk>/',views.CommentDetailView.as_view(),name="commenDetail"),
    # path('getcomment/<slug:slug>/',views.getComments,name="getComments"),

]
