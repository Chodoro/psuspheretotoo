"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg import views

from studentorg.views import OrgmemberList, OrgmemberCreateView , OrgmemberUpdateView , OrgmemberDeleteView

from studentorg.views import StudentList, StudentCreateView , StudentUpdateView , StudentDeleteView

from studentorg.views import CollegeList, CollegeCreateView , CollegeUpdateView , CollegeDeleteView 

from studentorg.views import ProgramList, RankedOrganizationChart, DoughnutChart, HorizontalBarChart, LineCountbyMonth, PieCountStudentsPerProgram, ProgramCreateView , ChartView, ProgramUpdateView , ProgramDeleteView

from django.urls import path, re_path

from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name  = 'organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name = 'organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name = 'organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name = 'organization-delete' ),

    path('program_list', ProgramList.as_view(), name  = 'program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name = 'program-add'),
    path('program_list/<pk>', ProgramUpdateView.as_view(), name = 'program-update'),
    path('program_list/<pk>/delete', ProgramDeleteView.as_view(), name = 'program-delete' ),


    path('orgmember_list', OrgmemberList.as_view(), name  = 'orgmember-list'),
    path('orgmember_list/add', OrgmemberCreateView.as_view(), name = 'orgmember-add'),
    path('orgmember_list/<pk>', OrgmemberUpdateView.as_view(), name = 'orgmember-update'),
    path('orgmember_list/<pk>/delete', OrgmemberDeleteView.as_view(), name = 'orgmember-delete' ),

    path('student_list', StudentList.as_view(), name  = 'student-list'),
    path('student_list/add', StudentCreateView.as_view(), name = 'student-add'),
    path('student_list/<pk>', StudentUpdateView.as_view(), name = 'student-update'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name = 'student-delete' ),

    path('college_list', CollegeList.as_view(), name  = 'college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name = 'college-add'),
    path('college_list/<pk>', CollegeUpdateView.as_view(), name = 'college-update'),
    path('college_list/<pk>/delete', CollegeDeleteView.as_view(), name = 'college-delete' ),

    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountStudentsPerProgram, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('horizontalChart/', HorizontalBarChart, name='chart'),
    path('doughnutChart/', DoughnutChart, name='chart'),
    path('scatterChart/', RankedOrganizationChart, name='chart'),
    
    re_path(r'⌃login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'⌃logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
]