from django.conf.urls import url
from gp.views import *
from django.conf import settings

urlpatterns = [
			url(r'^$', homeRedirect),
			url(r'^complaint/post/$',PostComplaint.as_view(),name = 'postcomplaint'),
			url(r'^accounts/login/$',LoginView.as_view(),name = 'login'),
			url(r'^complaints/view/$',ViewComplaintByDomain.as_view(),name= 'complaints'),
			url(r'^accounts/home/$',HomeView.as_view(),name='homepage'),
			url(r'^upvote/complaint/',Upvotes,name = 'upvote'),
			url(r'^mycomplaints/$',viewMyComplaints.as_view(),name='mycomplaints'),
			url(r'^submit/suggestion/$', submitSuggestion, name='submitsuggestion')		
		]