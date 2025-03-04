from ipaddress import *
for mask in range(1, 32 + 1):
    net1 = ip_network(f'84.77.47.132/{mask}', 0)
    net2 = ip_network(f'84.77.48.132/{mask}', 0)
    if net1 != net2:
        print(mask, net1.netmask, f'{net1.netmask:b}')
#3 слева байт будет иметь вид 11110000
print('Result:', int('11110000', 2))
