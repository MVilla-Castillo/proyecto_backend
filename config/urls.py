from django.urls import include, path

urlpatterns = [
    path('', include('cowork.urls')),
]

handler404 = 'cowork.views.error_404'