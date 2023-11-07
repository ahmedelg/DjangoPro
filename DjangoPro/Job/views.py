from django.shortcuts import render
# Models
from .models import Job

# Create your views here.
# Jobs List
def job_list(request):
    jobs_list=Job.objects.all()
    # print(jobs_list)
    # Pass Models' Data to Template
    context={
        'Jobs':jobs_list
    }
    return render(request,'Job/all_jobs.html',context)  

# Job Details
def job_details(request, id):
    context={}
    return render(request,'Job/job_details.html',context)
    