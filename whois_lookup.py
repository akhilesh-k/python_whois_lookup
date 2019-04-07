import whois
import socket

def whois_lookup(url):
	w=whois.whois(url)
	print("\nDomain Expiry Date: {}".format(w['expiration_date']))
	print("Domain Name: {}\n".format(w['domain_name']))
	print("IP Address: {}\n".format(socket.gethostbyname(url)))
	e=w['expiration_date']
	d=w['domain_name']
	ip=socket.gethostbyname(url)
	a=[e,d,ip]
	#print("Hello1")
	return a

#a=whois_lookup("www.cybervie.com")