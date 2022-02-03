from django.urls import path
from data import views

urlpatterns = [
    path('', views.UserEmployeeCreateView.as_view(), name='user_employee'),

    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    #path('register', views.RegisterView.as_view(), name='register'),

    path('education-create', views.EducationCreateView.as_view(), name='education_create'),
    path('experience-create', views.ExperienceCreateView.as_view(), name='experience_create'),
    path('managerdata-create', views.AgentManagerCreateView.as_view(), name='managerdata_create'),

    path('useremployee-update/<int:pk>', views.UserEmployeeUpdateView.as_view(), name='user_employee_update'),
    path('education-update/<int:pk>', views.EducationUpdateView.as_view(), name='education_update'),
    path('experience-update/<int:pk>', views.ExperienceUpdateView.as_view(), name='experience_update'),
    path('managerdata-update/<int:pk>', views.AgentManagerUpdateView.as_view(), name='managerdata_update'),

    path('useremployee-delete/<int:pk>', views.UserEmployeeDeleteView.as_view(), name='user_employee_delete'),
    path('education-delete/<int:pk>', views.EducationDeleteView.as_view(), name='education_delete'),
    path('experience-delete/<int:pk>', views.ExperienceDeleteView.as_view(), name='experience_delete'),
    path('managerdata-delete/<int:pk>', views.AgentManagerDeleteView.as_view(), name='managerdata_delete'),

    path('useremployee-detail/<int:pk>', views.UserEmployeeDetailView.as_view(), name='user_employee_detail'),
    path('education-detail/<int:pk>', views.EducationDetailView.as_view(), name='education_detail'),
    path('experience-detail/<int:pk>', views.ExperienceDetailView.as_view(), name='experience_detail'),
    path('managerdata-detail/<int:pk>', views.AgentManagerDetailView.as_view(), name='managerdata_detail'),

    path('useremployee-list', views.UserEmployeeListView.as_view(), name='user_employee_list'),
    path('education-list', views.EducationListView.as_view(), name='education_list'),
    path('experience-list', views.ExperienceListView.as_view(), name='experience_list'),
    path('managerdata-list', views.AgentManagerListView.as_view(), name='managerdata_list'),

]