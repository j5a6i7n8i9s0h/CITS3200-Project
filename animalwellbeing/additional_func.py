
def standardise_keys(dictionary): 
	dict2 = dictionary.copy()
	dict2['contact_details'] = dict((''.join(x for x in key.title() if not x.isspace() and x!=':'), val)  for key,val in dict2['contact_details'].items())
	return dict2