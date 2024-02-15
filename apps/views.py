from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from apps.models import People


class PeopleListView(ListView):
    template_name = 'apps/users/users_list.html'
    queryset = People.objects.order_by('-id')
    context_object_name = 'people'

class PersonDeleteView(DeleteView):
    template_name = 'apps/users/users_list.html'
    model = People
    queryset = People.objects.all()
    success_url = reverse_lazy('list_people')

class UserUpdateView(UpdateView):
    template_name = 'update_person.html'
    form_class = People
    model = People
    success_url = reverse_lazy('list_people')



