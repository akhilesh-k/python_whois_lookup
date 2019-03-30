import whois
import socket

def whois_lookup(url):
	w=whois.whois(url)
	print("\nDomain Expiry Date: {}".format(w['expiration_date']))
	print("Domain Nmae: {}\n".format(w['domain_name']))
	print("IP Address: {}\n".format(socket.gethostbyname(url)))

print("Enter website name")
url=input()
whois_lookup(url)