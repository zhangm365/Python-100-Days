import ssl
import builtwith
import whois

ssl._create_default_https_context = ssl._create_unverified_context
print(builtwith.parse('http://www.github.com/'))
print(whois.whois('http://www.github.com/'))