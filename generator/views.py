from django.shortcuts import render
from .models import ModelCV


# Create your views here.


def ResumeView(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        role = request.POST.get('role', "")
        summary = request.POST.get('summary', "")
        university = request.POST.get('university', "")
        current_role = request.POST.get('current_role', "")
        degree = request.POST.get('degree', "")
        skills = request.POST.get('skills', "")
        resume = ModelCV(name=name, email=email, phone=phone, role=role, summary=summary, university=university,
                         current_role=current_role, degree=degree, skills=skills)
        resume.save()
    return render(request, 'generator/resume.html')


def DesignView(request, id):
    application = ModelCV.objects.get(pk=id)
    context = {
        'applicant': application
    }

    return render(request, 'generator/design.html', context)
