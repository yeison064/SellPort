from django.shortcuts import render
from .models import (
    AboutMe,
    mySkills,
    PersonalInformation,
    whatIDo,
    TechSkills,
    ProfSkills,
    educationalEx,
    profEx,
    featuredPost
)
from .models import contact
from .models import testimonials
# Create your views here.

def index(request):
    if request.method == 'POST':
        print('POST REQUEST')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if fname and lname and email and message:
            contact_object = contact.objects.create(fname=fname,lname=lname,email=email,message=message)
            contact_object.save()
        print(fname,lname,email,message)
    return render(request,'core/index.html',{
        'about_data': AboutMe.objects.all()[0],
        'skill_data': mySkills.objects.all(),
        'personal_data': PersonalInformation.objects.all()[0],
        'what_i_do_data': whatIDo.objects.all(),
        'tech_skills': TechSkills.objects.all(),
        'prof_skills': ProfSkills.objects.all(),
        'education_data': educationalEx.objects.all(),
        'professional_data': profEx.objects.all(),
        'testimonial': testimonials.objects.all(),
        'post' : featuredPost.objects.all()
    })