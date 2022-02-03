
from django.shortcuts import redirect, render
from dataclasses import fields
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView
from django.views.generic.edit import FormView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import UserEmployeeForm, AgentManagerForm, EducationForm, ExperienceForm, LoginForm
from .models import UserEmployee, Education, Experience, AgentManager


class LoginView(BaseLoginView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'login.html'
    from_class = LoginForm   
   
    def get_success_url(self):
        
        if self.request.user is not None:
            if self.request.user.is_superuser:
                return redirect('managerdata_create')
            else:
                return redirect('user_employee_list')


class UserEmployeeFormView(FormView):
    model = UserEmployee
    form_class = UserEmployeeForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('useremployee_list')

    def form_valid(self, form):
        form.save()

class EducationFormView(FormView):
    model = Education
    form_class = EducationForm
    template_name = 'education_form.html'
    success_url = reverse_lazy('user_employee')

    def form_valid(self, form):
        form.save()


class ExperienceFormView(FormView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experiance_form.html'
    success_url = reverse_lazy('user_employee')

    def form_valid(self, form):
        form.save()

    
class AgentManagerFormView(FormView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'managerdata.html'
    success_url = reverse_lazy('user_employee')

    def form_valid(self, form):
        form.save()

 
class UserEmployeeCreateView(CreateView):
    model = UserEmployee
    form_class = UserEmployeeForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('useremployee_list')


class EducationCreateView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'education_form.html'
    success_url = reverse_lazy('user_employee')


class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experiance_form.html'
    success_url = reverse_lazy('user_employee')


class AgentManagerCreateView(CreateView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'managerdata.html'
    success_url = reverse_lazy('user_employee')


class UserEmployeeUpdateView(UpdateView):
    model = UserEmployee
    form_class = UserEmployeeForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_employee')


class EducationUpdateView(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'education_form.html'
    success_url = reverse_lazy('user_employee')


class ExperienceUpdateView(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'data/experiance_form.html'
    success_url = reverse_lazy('user_employee')


class AgentManagerUpdateView(UpdateView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'data/managerdata_form.html'
    success_url = reverse_lazy('user_employee')


class UserEmployeeDeleteView(DeleteView):
    model = UserEmployee
    form_class = UserEmployeeForm
    template_name = 'data/useremployee_confirm_delete.html'
    success_url = reverse_lazy('user_employee')


class EducationDeleteView(DeleteView):
    model = Education
    form_class = EducationForm
    template_name = 'data/education_confirm_delete.html'
    success_url = reverse_lazy('user_employee')


class ExperienceDeleteView(DeleteView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'data/experiance_confirm_delete.html'
    success_url = reverse_lazy('user_employee')


class AgentManagerDeleteView(DeleteView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'data/managerdata_confirm_delete.html'
    success_url = reverse_lazy('user_employee')


class UserEmployeeDetailView(DetailView):
    model = UserEmployee
    form_class = UserEmployeeForm
    template_name = 'data/useremployee_detail.html'
    success_url = reverse_lazy('user_employee')


class EducationDetailView(DetailView):
    model = Education
    form_class = EducationForm
    template_name = 'data/education_detail.html'
    success_url = reverse_lazy('user_employee')


class ExperienceDetailView(DetailView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'data/experiance_detail.html'
    success_url = reverse_lazy('user_employee')


class AgentManagerDetailView(DetailView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'data/managerdata_detail.html'
    success_url = reverse_lazy('user_employee')


class UserEmployeeListView(ListView):
    model = UserEmployee
    form_class = UserEmployeeForm
    template_name = 'data/user_list.html'


class EducationListView(ListView):
    model = Education
    form_class = EducationForm
    template_name = 'data/education_list.html'


class ExperienceListView(ListView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'data/experiance_list.html'


class AgentManagerListView(ListView):
    model = AgentManager
    form_class = AgentManagerForm
    template_name = 'data/managerdata_list.html'
