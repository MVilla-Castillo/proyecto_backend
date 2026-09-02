from django.urls import include, path

urlpatterns = [
    path('', include('cowork.urls')),
]
