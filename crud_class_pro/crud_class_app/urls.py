from django.urls import path
#from .views import View_Data,Add_Student,EditStudent,Delete_Student
from crud_class_app import views as core_views

urlpatterns = [
    path('', core_views.View_Data.as_view(), name='view-data'),
    path('add/', core_views.Add_Student.as_view(), name='add'),
    path('edit-student/<int:id>/', core_views.EditStudent.as_view(), name='edit-student'),
    path('delete-student/<int:id>/', core_views.Delete_Student.as_view(), name='delete-student'),
]