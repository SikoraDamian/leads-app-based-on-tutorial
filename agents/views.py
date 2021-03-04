from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent

class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        return Agent.objects.all()
