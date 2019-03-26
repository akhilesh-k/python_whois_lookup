import whois

def whois(url):
	w=whois.whois(url)
	print(w['expiration_date'])
	print(w['domain_name'])


print("Enter website name")
url=input()
whois(url)