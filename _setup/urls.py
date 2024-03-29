"""_setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from django.contrib import admin
from django.urls import path, include
from softdesk.views import ProjectViewset, UserViewset,ProjectUserViewset,IssueViewset,CommentViewset

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewset, basename='projects')
project_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
project_router.register(r'users' , ProjectUserViewset, basename='users' )
issues_router = routers.NestedSimpleRouter(router, r'projects', lookup='projects')
issues_router.register(r'issues', IssueViewset, basename='issues')
comments_router = routers.NestedSimpleRouter(issues_router, r'issues',lookup='issues' )
comments_router.register(r'comments', CommentViewset, basename='comments')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(comments_router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserViewset.as_view({'post': 'create'}))
]
