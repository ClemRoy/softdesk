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
router.register(r'project', ProjectViewset, basename='project')
project_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
project_router.register(r'users' , ProjectUserViewset, basename='users' )
issue_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
issue_router.register(r'issue', IssueViewset, basename='issue')
comment_router = routers.NestedSimpleRouter(issue_router, r'issue',lookup='issue' )
comment_router.register(r'comment', CommentViewset, basename='comment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('', include(comment_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserViewset.as_view({'post': 'create'}))
]
