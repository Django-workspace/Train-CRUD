from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    
    path('create/',views.Trainee_save , name="create" ),
    path('',views.All_Trainees, name="All_Trainee"),
    path('Update/<id>/',views.Trainee_update, name="Update"),
    path('Delete/<id>/',views.deleteTrainees, name="Delete")

]
