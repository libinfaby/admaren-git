from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    SnippetOverviewAPIView, SnippetDetailAPIView, SnippetCreateAPIView, 
    SnippetUpdateAPIView, SnippetDeleteAPIView,
    TagListAPIView, TagDetailAPIView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('snippet/overview/', SnippetOverviewAPIView.as_view(), name='snippet-overview'),
    path('snippet/detail/<int:pk>/', SnippetDetailAPIView.as_view(), name='snippet-detail'),
    path('snippet/create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
    path('snippet/update/<int:pk>/', SnippetUpdateAPIView.as_view(), name='snippet-update'),
    path('snippet/delete/<int:pk>/', SnippetDeleteAPIView.as_view(), name='snippet-delete'),
    
    path('tag/list/', TagListAPIView.as_view(), name='tag-list'),
    path('tag/detail/<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
]