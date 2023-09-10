from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Job
from .form import *

def job_list(request):
    job_list = Job.objects.all().order_by('-published_at')
    paginator = Paginator(job_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj}
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
            form = ApplyForm()                    # <= 1 idea
            # return redirect(f'/jobs/{slug}')    # <= 2 idea
    else:
        form = ApplyForm()

    context = {'job':job_detail, 'form1':form}
    return render(request, 'job/job_detail.html', context)

def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()                    
            return redirect('/jobs')            
    else:
        form = JobForm()
    return render(request, 'job/add_job.html',{'form2':form})