from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView
from users.models import AddUser
from users.forms import UserForm



class UserListView(ListView):
    model = AddUser
    template_name = 'user_list.html'

class AddUserView(FormView):

    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()  #veido jaunu ierakstu DB no ievadītajiem datiem .save() komanda

        response = super().form_valid(form)
        return response

class GetUserView(DetailView):
    model = AddUser
    template_name = 'get_user.html'


class DeleteUserView(DeleteView):
    model = AddUser
    template_name = 'delete_user.html'
    success_url = '/'


class EditUserView(UpdateView):
    model = AddUser
    fields = [
        'username',
        'email'
    ]
    template_name = 'update_user.html'
    success_url = '/'
