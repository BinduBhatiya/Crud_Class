from django.urls import path
from .views import View_Data,Add_Student,EditStudent,Delete_Student
#from .views import View as crud_class_app_views
urlpatterns = [
    path('', View_Data.as_view(), name='view-data'),
    path('add/', Add_Student.as_view(), name='add'),
    path('edit-student/<int:id>/', EditStudent.as_view(), name='edit-student'),
    path('delete-student/<int:id>/', Delete_Student.as_view(), name='delete-student'),
]