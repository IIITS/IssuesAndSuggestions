from django.contrib import admin
from gp.models import Complaint ,Domain, Upvote
# Register your models here.
admin.site.register(Complaint)
admin.site.register(Domain)
admin.site.register(Upvote)
