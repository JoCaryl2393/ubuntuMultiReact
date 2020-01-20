from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers                    # add this
from Crud import views  

router = routers.DefaultRouter()                      # add this
router.register(r'posts', views.PostView, 'Crud')     # add this

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls)),                # add this
]