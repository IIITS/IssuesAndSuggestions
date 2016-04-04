from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from gp.models import Complaint, Domain, Upvote
from gp.forms import LoginForm, postComplaintForm
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import logout
from gp.methods import Is_incharge
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.mail import send_mail
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator

# Create your views here.
class LoginView(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = settings.LOGIN_REDIRECT_URL
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	auth_login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to) 
	
	def form_invalid(self,form):	
		return super(LoginView, self).form_invalid(form)
	@method_decorator(sensitive_post_parameters())	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_active:
			return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
		return super(LoginView,self).dispatch(*args, **kwargs)
	def get_context_data(self, **kwargs):
			context = super(LoginView,self).get_context_data(**kwargs)
			return context	


class HomeView(TemplateView):
	template_name ='home.html'

	def dispatch(self,*args,**kwargs):
		return super(HomeView,self).dispatch(*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)

class PostComplaint(FormView):
	form_class = postComplaintForm
	template_name = 'post_complaint.html'
	success_url = '/complaints/view/'
	
	def dispatch(self,*args,**kwargs):
		return super(PostComplaint,self).dispatch(*args,**kwargs)
	
	def form_valid(self,form):
			domain = form.cleaned_data['domain'].encode('utf-8')
			try:
				domain_obj = Domain.objects.get(name=str(domain))
			except DoesNotExist:
				domain_obj= Domain.objects.all()[0] 

				
			title = form.cleaned_data['title'].encode('utf-8')
			description = form.cleaned_data['description'].encode('utf-8')
			#send_mail('Issue Registered in the portal.Sub = '+title , description,'IandS@iiits.in',domain_obj.Incharge.split(','),fail_silently = False)
			c = Complaint(title=title,description=description,domain=domain_obj,posted_by = self.request.user)
			c.save()
			redirect_to = self.success_url
			return super(PostComplaint,self).form_valid(form)

	def get_context_data(self, **kwargs):
			context = super(PostComplaint,self).get_context_data(**kwargs)
			return context 

	def form_invalid(self,form):
			return self.render_to_response(self.get_context_data(form=form))	



class ViewComplaintByDomain(TemplateView):
	template_name = 'complaints.html'

	def dispatch(self,*args,**kwargs):
		return super(ViewComplaintByDomain,self).dispatch(*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(ViewComplaintByDomain,self).get_context_data(**kwargs)
		get_by_domain = self.request.GET.get('get_by_domain')

		if get_by_domain == 'All' or get_by_domain == None:
			c = Complaint.objects.all()

		else:
			c = Complaint.objects.filter(domain = get_by_domain)
	

		context['complaints'] = c	
		
		return context


class viewMyComplaints(TemplateView):
	template_name = 'mycomplaints.html'

	def dispatch(self,*args,**kwargs):
		return super(viewMyComplaints,self).dispatch(*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(viewMyComplaints,self).get_context_data(**kwargs)
		user = self.request.user
		c = Complaint.objects.filter(posted_by = user)

		context['mycomplaints'] = c 
		
		return context


def Upvotes(request):
	 
	 ID = request.GET.get('ID')
	 c = Complaint.objects.get(id=int(ID))
	 userId = request.user
	 try:
	 	up = Upvote(cid = c, uid = userId)
	 	up.save()
	 	cup = c.upvote()
	 	c.save()
	 	return HttpResponse(cup)
	 except IntegrityError:
			return HttpResponse("You already upvoted,"+str(c.getUpvotes()))
	 
	 

			

	 

