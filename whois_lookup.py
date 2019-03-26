import whois

w=whois.whois("google.co.in")
print(w['expiration_date'])
