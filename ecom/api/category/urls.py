from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.CategoryViewSet)
#router.register(r'accounts', AccountViewSet)
urlpatterns = [
    path('', include(router.urls))
]