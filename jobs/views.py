from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ApplyForm
from .models import Jobs


# Create your views here.
def home(request):
    jobs = Jobs.objects.all()
    context = {"jobs": jobs}
    return render(request, 'jobs/home.html', context)


def apply(request, job_id):
    job = Jobs.objects.get(id=job_id)
    jobs = Jobs.objects.all()
    form = ApplyForm()
    return render(request, 'jobs/apply.html', {"job": job, "jobs": jobs, "form": form})


def save_apply(request):
    if request.method == "POST" and request.FILES.get("resume"):
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = messages.success(
                request, "Successfully Subscribed", extra_tags="alert"
            )
            return redirect(reverse("job:home"), {"messages": message})
        else:
            context = {"form": form}
            return render(request, "jobs/apply.html", context)
    return render(request, 'jobs/home.html')
