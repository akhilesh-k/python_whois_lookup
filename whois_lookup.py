import whois

w=whois.whois("google.co.in")
print(w['expiration_date'])
print(w['domain_name'])
