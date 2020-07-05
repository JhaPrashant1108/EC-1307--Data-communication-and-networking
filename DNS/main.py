import dns
import dns.resolver
import sys

result = dns.resolver.resolve(sys.argv[1], 'A')
for ipval in result:
    print('IP', ipval.to_text())

result = dns.resolver.resolve(sys.argv[1], 'CNAME')
for ipval in result:
    print('CNAME target address', ipval.to_text())