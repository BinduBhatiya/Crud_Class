from django.shortcuts import redirect,render
from django.views import View
from .models import Student
from .forms import AddStudentForm

# Create your views here.
class View_Data(View):
    def get(self,request):
        stu_data = Student.objects.all()
        return render(request, 'view_data.html', {'studata':stu_data})
class Add_Student(View):
    def get(self,request):
        fm = AddStudentForm
        return render(request, 'add.html', {'form':fm})
    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'add.html', {'form':fm})
class EditStudent(View):
    def get(self,request,id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'edit-student.html', {'form':fm})
    def post(self,request,id):
        stu = Student.objects.get(id=id) 
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
class Delete_Student(View):
    def get(self,request,id):
        data = Student.objects.get(id=id)
        data.delete()
        return redirect('/')
    
        
        

            
        

    