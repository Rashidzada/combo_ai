from django.urls import path,include
from . import views
from .import routers
urlpatterns = [
    path('', views.index, name='index'),
    path('add-tool/', views.add_tool, name='add_tool'),
    path('api/', include(routers.router.urls)),  # API routes
]