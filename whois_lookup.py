import whois

print("Enter website name")
url=input()
w=whois.whois(url)
print(w['expiration_date'])
print(w['domain_name'])
