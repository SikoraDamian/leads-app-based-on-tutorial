from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf.urls.static import static
from leads.views import LandingPagesView, SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', LandingPagesView.as_view(), name='landing-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, dicument_root=settings.STATIC_ROOT)
