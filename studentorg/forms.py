from django.forms import ModelForm
from django import forms
from .models import Organization, Orgmember, Student, Program, College

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgmemberForm(ModelForm):
    class Meta:
        model = Orgmember
        fields = "__all__"

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"