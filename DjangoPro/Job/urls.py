from django.urls import include, path
# Job Views
from . import views

urlpatterns = [
    # Jobs
    path('', views.job_list),
    # Specific Job
    path('<int:id>', views.job_details)
]