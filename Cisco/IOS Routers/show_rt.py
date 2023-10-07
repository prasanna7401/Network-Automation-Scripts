from netmiko import ConnectHandler
from threading import Thread

with open('router_ip.txt') as device_file:
    device_list = device_file.read().splitlines()

def show_in(device_detail):
    connection = ConnectHandler(**device_detail)
    
    with open('cr-cmd.txt') as cmds:
        cmd_list = cmds.read().splitlines()
        
        for cmd in cmd_list:
            output = connection.send_command(cmd)
            
            prompt = connection.find_prompt() # returns hostname#
            hostname = prompt[:-1]
            show_op_filename = hostname+'.txt'
            output_filepath = 'outputs\\'+show_op_filename
            
            with open(show_in_filename,'a+') as show_op:
                show_op.write(output)
            print('Sending command - {} to {}\n'.format(cmd, hostname))
    
    connection.disconnect()
    print('Connection terminated with '+hostname)
    print('#'*60)

thread_list = []

for device_ip in device_list:
    device_detail = {'host': device_ip, 'device_type':'cisco_ios',
                    'username':'admin', 'password':'XXXX', 'secret':'XXXX', 'verbose':True}
    
    th = Thread(target=show_in,args=(device_detail,))
    thread_list.append(th)    

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
