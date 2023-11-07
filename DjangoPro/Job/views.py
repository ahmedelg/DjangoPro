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
    # Specific Job
    job_dependOn_id=Job.objects.get(id=id)
    # job_dependOn_id = Job.objects.filter(id=id)

    # Filter() not same get() about What does each one return?

    # print(.title)
    # print(job_dependOn_id.title)
    # print(job_dependOn_id)
    context={
        'job':job_dependOn_id
    }
    return render(request,'Job/job_details.html', context)
    