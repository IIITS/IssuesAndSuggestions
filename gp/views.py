from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from gp.models import Complaint, Domain, Upvote
from gp.forms import *
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import logout
from gp.methods import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.mail import send_mail
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from methods import Is_incharge
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class LoginView(FormView):
	form_class = LoginForm
	template_name = 'login.html'
	success_url = settings.LOGIN_REDIRECT_URL
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	login(self.request, form.get_user())
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
	template_name ='complaints.html'
	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(HomeView,self).dispatch(*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)
		context={}
		AllPosts = Complaint.objects.order_by('-posted_on')
		Posts = putStatus(AllPosts)
		user = self.request.user
		Posts = putUpvotes(Posts, user)
		Posts = putIncharge(Posts,user)
		context['posts']=Posts
		context['form']=SuggestionForm
		return context
	
class PostComplaint(FormView):
	form_class = PostComplaintForm
	template_name = 'post_complaint.html'
	success_url = settings.LOGIN_REDIRECT_URL
	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(PostComplaint,self).dispatch(*args,**kwargs)
	
	def form_valid(self,form):
			domain = form.cleaned_data['domain'].encode('utf-8')
			try:
				domain_obj = Domain.objects.get(name=str(domain))
			except ObjectDoesNotExist:
				domain_obj= Domain.objects.all()[0] 

				
			title = form.cleaned_data['title'].encode('utf-8')
			description = form.cleaned_data['description'].encode('utf-8')
			# form.cleaned_data['hostel'] returns empty string when checked domain is Academic or Mess
			# when Hostel is checked, We have show it only to Girls group or only to boys group
			resultSendIncharge = send_mail('Issue Registered in the portal with title \"' + title + '\"', description,'tremblerz@gmail.com', domain_obj.Incharge.split(','), fail_silently = False)
			resultSendApplicant = send_mail('Your Issue with title \"' + title + '\"' + ' has been registered', "Thanks for expressing your inconvenience.\nYour issue has been registered on the website and email has been sent to faculty incharge\n\nThanks and Regards\nIT Support",'tremblerz@gmail.com', [self.request.user.email], fail_silently=False)
			#TODO: Check the return values from send_mail
			c = Complaint(title=title,description=description,domain=domain_obj,posted_by = self.request.user)
			c.save()
			return super(PostComplaint,self).form_valid(form)

	def get_context_data(self, **kwargs):
			context = super(PostComplaint,self).get_context_data(**kwargs)
			return context 

	def form_invalid(self,form):
			print "here"
			return self.render_to_response(self.get_context_data(form=form))	



class ViewComplaintByDomain(FormView):
	template_name = 'complaints.html'
	form_class = Email_Form
	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(ViewComplaintByDomain,self).dispatch(*args,**kwargs)
	def form_valid(self,form):
		recep = form.cleaned_data['recep'].encode('utf-8')
		bod =  form.cleaned_data['bod'].encode('utf-8')
		return super(ViewComplaintByDomain,self).form_valid(form)	
	
				
		
	def get_context_data(self,**kwargs):
		context = super(ViewComplaintByDomain,self).get_context_data(**kwargs)
		get_by_domain = self.request.GET.get('get_by_domain')

		if get_by_domain == 'All' or get_by_domain == None:
			c = Complaint.objects.all()
		else:
			c = Complaint.objects.filter(domain = get_by_domain).order_by('-posted_on')
		Posts = putStatus(c)
		user = self.request.user
		posts = putIncharge(Posts, user)
		posts = putUpvotes(posts, user)
		context['posts'] = posts
		context['form'] = Email_Form
		return context

	def form_invalid(self,form):
		return self.render_to_response(self.get_context_data(form=form))

class viewMyComplaints(TemplateView):
	template_name = 'complaints.html'
	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(viewMyComplaints,self).dispatch(*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(viewMyComplaints,self).get_context_data(**kwargs)
		user = self.request.user
		c = Complaint.objects.filter(posted_by = user)

		context['mycomplaints'] = c 
		
		return context

@login_required
def Upvotes(request):
	ID = request.GET.get('ID')
	status = request.GET.get('status').split()[1]
	c = Complaint.objects.get(id=int(ID))
	user = request.user

	if status == "not-upvoted":
		if not Upvote.objects.filter(complaint=c).filter(user=user).exists():
		 	up = Upvote(complaint = c, user = user)
		 	up.save()
			return HttpResponse("upvoted,"+str(len(Upvote.objects.filter(complaint=c))))
		return HttpResponse("not-upvoted,"+str(len(Upvote.objects.filter(complaint=c))))
	elif status == "upvoted":
		up = Upvote.objects.filter(complaint=c).filter(user=user)
		if len(up) == 1:
			up[0].delete()
	 		return HttpResponse("not-upvoted,"+str(len(Upvote.objects.filter(complaint=c))))
		return HttpResponse("upvoted,"+str(len(Upvote.objects.filter(complaint=c))))
			

@login_required
def submitSuggestion(request):
	 user = request.user
	 try:
		 issue = Complaint.objects.get(id=request.GET.get('ID'))
		 submission = Submission(
	 		complaint=issue,
	 		author=user,
	 		suggestion=request.GET.get('suggestion')
	 		)
	 	 submission.save()
	 except ObjectDoesNotExist as Error:
	 	return HttpResponse("500")
	 except KeyError as Error:
	 	return HttpResponse("500")
	 return HttpResponse("200")

def homeRedirect(request):
	return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
@login_required
def getSuggestions(request):
	user = request.user
	cid = request.GET['cid']
	begin = int(request.GET['begin'])
	end =  int(request.GET['end'])
	complaint = Complaint.objects.get(id=cid)
	try:
		suggestions = Suggestion.objects.filter(complaint=complaint)[begin:end].value_list()
	except IndexError as Error:
		suggestions = Suggestions.objects.filter(complaint=complaint)[begin:].value_list()	
	return HttpResponse(suggestions)

@login_required
def signout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGOUT_URL)
		

