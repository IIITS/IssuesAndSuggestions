from gp.models import Domain
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