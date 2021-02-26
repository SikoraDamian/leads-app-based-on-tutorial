from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPagesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('', LandingPagesView.as_view(), name='landing-page'),
]
