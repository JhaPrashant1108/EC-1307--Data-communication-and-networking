from pysnmp.entity.rfc3413.oneliner import cmdgen
import time
import matplotlib.pyplot as plt

cmdGen = cmdgen.CommandGenerator()

snmp_community = cmdgen.CommunityData('public')
snmp_ip =  cmdgen.UdpTransportTarget(('10.10.88.110', 161))
snmp_oids = [".1.3.6.1.4.1.9.2.2.1.1.6.3",".1.3.6.1.4.1.9.2.2.1.1.8.3"]

slots = 0
input_rates = []
output_rates = []
while slots <= 50:
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(snmp_community, snmp_ip, *snmp_oids)
    print(varBinds)
    input_rate = str(varBinds[0]).split("=")[1].strip()
    output_rate = str(varBinds[1]).split("=")[1].strip()

    input_rates.append(input_rate)
    output_rates.append(output_rate)

    time.sleep(6)
    slots = slots + 1
    print(slots)

time_range = range(0, slots)

print(input_rates)
print(output_rates)
# plt.figure()
plt.plot(time_range, input_rates, label="input rate")
plt.plot(time_range, output_rates, label="output rate")
plt.xlabel("time slot")
plt.ylabel("Traffic Measured in bps")
plt.title("Interface gig0/0/2 Traffic")