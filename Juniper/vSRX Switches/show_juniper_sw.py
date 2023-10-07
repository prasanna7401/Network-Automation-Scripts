from netmiko import ConnectHandler
from threading import Thread

with open('juniper_sw_ip.txt') as device_file:
    device_list = device_file.read().splitlines()

def show_in(device_detail):
    connection = ConnectHandler(**device_detail)
    
    prompt = connection.find_prompt() # returns hostname#
    prompt = prompt[:-1] #username@devicename
    hostname = prompt[prompt.find('@')+1:]
    show_output_filename = hostname+'.txt'
    output_path = 'Output\\'+show_output_filename
    with open('js-cmd.txt') as cmds:
        cmd_list = cmds.read().splitlines()
        
        for cmd in cmd_list:
            output = connection.send_command(cmd)
            with open(output_path,'a+') as show_op:
                show_op.write(output)
                show_op.write('\n')
            print('Sending command - {} to {}\n'.format(cmd, hostname))
    
    connection.disconnect()
    print('Connection terminated with '+hostname)
    print('#'*60)

thread_list = []

for device_ip in device_list:
    device_detail = {'host': device_ip, 'device_type':'juniper_junos',
                    'username':'admin', 'password':'XXXXXXX', 'port':22, 'verbose':True}
    
    th = Thread(target=show_in,args=(device_detail,))
    thread_list.append(th)    

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()