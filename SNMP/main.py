from pysnmp import hlapi
import sys
from quicksnmp import *

arg = sys.argv
Password = ''
if len(arg)==2:
  Password = arg[1]
  

# Using SNMPv2c, we set the hostname of the remote device to 'SNMPHost'
set('10.0.0.1', {'1.3.6.1.2.1.1.5.0': 'SNMPHost'}, hlapi.CommunityData(Password))

# Using SNMPv2c, we retrieve the hostname of the remote device
print(get('10.0.0.1', ['1.3.6.1.2.1.1.5.0'], hlapi.CommunityData(Password)))

its = get_bulk_auto('10.0.0.1', [
    '1.3.6.1.2.1.2.2.1.2 ',
    '1.3.6.1.2.1.31.1.1.1.18'
    ], hlapi.CommunityData(Password), '1.3.6.1.2.1.2.1.0')
# We print the results in format OID=value
for it in its:
    for k, v in it.items():
        print("{0}={1}".format(k, v))
    # We leave a blank line between the output of each interface
    print('')


