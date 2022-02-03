
from django import forms
from data.models import UserEmployee, Education, Experience, AgentManager, Applicant
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.ModelForm):

    class Meta:
        model = UserEmployee
        fields = ('username', 'password')


class UserEmployeeForm(UserCreationForm):

    class Meta:
        model = UserEmployee
        fields = ['username','first_name','last_name',  'mobile_number', 'email']


class Applications(forms.ModelForm):

     class Meta:
        model = Applicant
        fields = ['name', 'fresher_expiriance', 'agent_socialmedia']


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['name','degree_name','collage_name', 'cgpa', 'name', 'per_10th','per_12th', 'stream']


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ['name', 'company_name', 'year_of_experience', 'work', 'domain', 'salary', 'name']


class AgentManagerForm(forms.ModelForm):

    class Meta:
        model = AgentManager
        fields = ['username', 'name', 'code', 'mobile_number', 'post']
