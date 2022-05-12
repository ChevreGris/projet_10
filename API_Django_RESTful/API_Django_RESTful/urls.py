from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from softdesk_app.views import ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'projects/(?P<project_id>[^/.]+)/issue/(?P<issue_id>[^/.]+)/comment', CommentViewSet, basename='comments')
router.register(r'projects/(?P<project_id>[^/.]+)/issue', IssueViewSet, basename='issues')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
