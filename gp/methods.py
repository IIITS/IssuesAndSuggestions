from gp.models import Domain, Complaint,  AssignedIssues, ClosedIssues, Upvote
from django.utils import timezone
PROCESS_HRS = 5
def get_list_of_domains():
	ret = list()
	domains = Domain.objects.all()
	for domain in domains:
		lister = list()
		lister.append(str(domain.name))
		lister.append(str(domain.name))
		ret.append( tuple(lister))	
	return tuple(ret)



def Is_incharge(domain,incharge):
	domain_obj = Domain.objects.get(name= domain)
	incharges = domain_obj.Incharge.split(',')
	if incharge in incharges:
		return True
	return False	

def getAllUnderProcess():
	Results = list()
	now = timezone.now()
	complaints = Complaint.objects.order_by('-posted_on')
	upissues = UpgradedIssues.objects.order_by('-upgrade_date')
	closedissues = ClosedIssues.objects.order_by('-closed_date')
	for com in complaints:
		if com not in upissues and com not in closedissues:
			if now - timezone.timedelta(hours=PROCESS_HRS) >= com.posted_on:
				Results.append(com)
	return Results	

def putStatus(QS):
	Results = list()
	for q in QS:
		D = dict()
		D["issue"] = q
		if ClosedIssues.objects.filter(pk=q.pk).exists():
			D['status'] = "Closed"
		elif AssignedIssues.objects.filter(pk=q.pk).exists():
			D['status'] = "Assigned"
		elif (timezone.now() - timezone.timedelta(hours=PROCESS_HRS) ) >= q.posted_on :
			D['status'] = "Under Process"
		else:
			D['status'] = "Registered"		
		Results.append(D)	
	return Results

def putIncharge(QS, user):
	for q in QS:
		complaint=q['issue']
		if(Is_incharge(complaint.domain,user)):
			q['incharge']=True
		else:
			q['incharge']=False
	return QS

def putUpvotes(QS, user):
	for q in QS:
		complaint=q['issue']
		if Upvote.objects.filter(cid=complaint,uid=user).exists():
			q['upvoted']=True
		else:
			q['upvoted']=False
	return QS									