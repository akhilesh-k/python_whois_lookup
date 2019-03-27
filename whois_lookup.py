import whois

def whois_lookup(url):
	w=whois.whois(url)
	print("\nDomain Expiry Date: {}".format(w['expiration_date']))
	print("Domain Nmae: {}\n".format(w['domain_name']))


print("Enter website name")
url=input()
whois_lookup(url)