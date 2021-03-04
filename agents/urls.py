from django.urls import path
from .views import AgentListView

app_name = 'agenta'

urlpatterns = [
    path('', AgentListView.as_view(), name='agents'),
]