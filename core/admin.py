from django.contrib import admin
from .models import (
    PersonalInformation,
    AboutMe,
    mySkills,
    whatIDo,
    TechSkills,
    ProfSkills,
    educationalEx,
    profEx,
    featuredPost,
    testimonials,
    contact
)
# Register your models here.

admin.site.register(PersonalInformation)
admin.site.register(AboutMe)
admin.site.register(mySkills)
admin.site.register(whatIDo)
admin.site.register(TechSkills)
admin.site.register(ProfSkills)
admin.site.register(educationalEx)
admin.site.register(profEx)
admin.site.register(featuredPost)
admin.site.register(testimonials)
admin.site.register(contact)