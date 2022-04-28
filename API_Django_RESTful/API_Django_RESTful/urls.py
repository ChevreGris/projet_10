"""API_Django_RESTful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from softdesk_app.views import UsersAPIView, ProjectsAPIView, ProjectViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import softdesk_app.views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/projects', ProjectViewSet, basename='projects')
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', UsersAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('api/signup/', softdesk_app.views.signup_page, name='signup'),
    path('api/login/', softdesk_app.views.login_page, name='login'),
    #path('api/projects/', ProjectsAPIView.as_view(), name='projects'),

    #path('api/projects/<int:id>/view/', softdesk_app.views.api_detail_project_view, name='view_projects'),
    #path('api/projects/update/{id}', softdesk_app.views.api_update_project_view, name='update_projects'),
    #path('api/projects/delete/{id}', softdesk_app.views.api_delete_project_view, name='delete_projects'),
    #path('api/projects/create', softdesk_app.views.api_create_project_view, name='create_projects'),

    

]

"""   
    path('api/projects/{id}/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/users/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/users/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/users/{id}', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}/comments/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}/comments/', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}/comments/{id}', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}/comments/{id}', UsersAPIView.as_view(), name=''),
    path('api/projects/{id}/issues/{id}/comments/{id}', UsersAPIView.as_view(), name=''),
"""