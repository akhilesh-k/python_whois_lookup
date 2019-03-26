import whois

def whois_lookup(url):
	w=whois.whois(url)
	print(w['expiration_date'])
	print(w['domain_name'])


print("Enter website name")
url=input()
whois_lookup(url)