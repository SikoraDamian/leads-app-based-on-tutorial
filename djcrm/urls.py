from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from leads.views import LandingPagesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('', LandingPagesView.as_view(), name='landing-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, dicument_root=settings.STATIC_ROOT)
