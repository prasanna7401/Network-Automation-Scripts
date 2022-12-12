import ipaddress

f1 = open('All Excluded Public IPs.txt','w')
total_IP = 0
with open('Public IP Subnet.txt','r') as f:
    subnets = f.read().splitlines()
    for ip_subnet in subnets:
        try:
            ip_net_add = ipaddress.ip_interface(ip_subnet)
        except ValueError:
            ip_subnet = ip_subnet+'/29' # If No subnet mentioned, they are classified under /29
            ip_net_add = ipaddress.ip_interface(ip_subnet)

        net = ipaddress.ip_network(ip_net_add.network)
        for x in net.hosts():
            f1.write(str(x)+'\n')
            total_IP+=1
print('Total IPs - ', total_IP)
f1.close()