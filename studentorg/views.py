from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from studentorg.forms import OrganizationForm, OrgmemberForm, StudentForm, ProgramForm, CollegeForm
from studentorg.models import Organization, Orgmember, Student, College, Program

from django.db import connection
from django.http import JsonResponse

from django.db.models import Count
from datetime import datetime

@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"


@method_decorator(login_required, name='dispatch')
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(college__college_name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')


@method_decorator(login_required, name='dispatch')
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')


@method_decorator(login_required, name='dispatch')
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')



@method_decorator(login_required, name='dispatch')
class OrgmemberList(ListView):
    model = Orgmember
    context_object_name = 'orgmember'
    template_name = "orgmem_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(student__firstname__icontains=query) |
                Q(student__lastname__icontains=query) |
                Q(student__middlename__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class OrgmemberCreateView(CreateView):
    model = Orgmember
    form_class = OrgmemberForm
    template_name = 'orgmem_add.html'
    success_url = reverse_lazy('orgmember-list')


@method_decorator(login_required, name='dispatch')
class OrgmemberUpdateView(UpdateView):
    model = Orgmember
    form_class = OrgmemberForm
    template_name = 'orgmem_edit.html'
    success_url = reverse_lazy('orgmember-list')


@method_decorator(login_required, name='dispatch')
class OrgmemberDeleteView(DeleteView):
    model = Orgmember
    template_name = 'orgmem_del.html'
    success_url = reverse_lazy('orgmember-list')



@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = "student_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) |
                Q(middlename__icontains=query) |
                Q(student_id__icontains=query) |
                Q(program__prog_name__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')


@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')



@method_decorator(login_required, name='dispatch')
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = "college_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(college_name__icontains=query)
        return qs


@method_decorator(login_required, name='dispatch')
class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')


@method_decorator(login_required, name='dispatch')
class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')


@method_decorator(login_required, name='dispatch')
class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')



class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = "program_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs


@method_decorator(login_required, name='dispatch')
class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')


@method_decorator(login_required, name='dispatch')
class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')


@method_decorator(login_required, name='dispatch')
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        pass

def PieCountStudentsPerProgram(request):
    query = '''
        SELECT p.prog_name, COUNT(s.id) as student_count
        FROM studentorg_student s
        JOIN studentorg_program p ON s.program_id = p.id
        GROUP BY p.prog_name
    '''
    data = {}
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    if rows:

        data = {program: count for program, count in rows}
    else:
        data = {}
    
    return JsonResponse(data)

def LineCountbyMonth(request):
    query = """
        SELECT 
            strftime('%m', date_joined) AS month,
            COUNT(*) AS member_count
        FROM 
            studentorg_orgmember
        WHERE 
            strftime('%Y', date_joined) = strftime('%Y', 'now')
        GROUP BY 
            strftime('%m', date_joined)
        ORDER BY 
            month;
    """
    
    month_names = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', 
        '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    result = {name: 0 for name in month_names.values()}
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        for month_num, count in cursor.fetchall():
            result[month_names[month_num]] = count

    return JsonResponse(result)

def HorizontalBarChart(request):

    result = {}


    org_members_count = Orgmember.objects.values('organization') \
        .annotate(student_count=Count('student_id'))
    

    for org in org_members_count:
        result[org['organization']] = org['student_count']
    
  
    return JsonResponse(result)


def DoughnutChart(request):
    result = {}

    college_members_count = Student.objects.values('program__college') \
        .annotate(student_count=Count('student_id')) 

   
    total_students = Student.objects.count()

  
    for college in college_members_count:
        college_obj = College.objects.get(id=college['program__college'])
        college_name = college_obj.college_name
        student_count = college['student_count']
        percentage = (student_count / total_students) * 100
        result[college_name] = {
            'student_count': student_count,
            'percentage': round(percentage, 2)
        }

  
    return JsonResponse(result)

def RankedOrganizationChart(request):
    
    query = """
        SELECT 
            c.college_name,
            COUNT(DISTINCT o.id) as organization_count,
            COUNT(DISTINCT s.id) as student_count
        FROM 
            studentorg_college c
        LEFT JOIN 
            studentorg_organization o ON c.id = o.college_id
        LEFT JOIN 
            studentorg_student s ON c.id = s.program_id
        GROUP BY 
            c.college_name
        ORDER BY 
            organization_count DESC
    """
    
    result = {
        'labels': [],
        'datasets': [{
            'label': 'Colleges',
            'data': [],
            'backgroundColor': []
        }]
    }
    
    colors = ["#1d7af3", "#f3545d", "#fdaf4b", "#28a745", "#6f42c1"]
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        for i, (college_name, org_count, student_count) in enumerate(cursor.fetchall()):
            result['labels'].append(college_name)
            result['datasets'][0]['data'].append({
                'x': org_count,
                'y': student_count,
                'r': 10 + (org_count * 2) 
            })
            result['datasets'][0]['backgroundColor'].append(colors[i % len(colors)])
    
    return JsonResponse(result)