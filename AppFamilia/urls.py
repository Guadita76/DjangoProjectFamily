from django.urls import include, path

from .views import datos_familia

urlpatterns = [

    path ("familia/" , datos_familia),
]