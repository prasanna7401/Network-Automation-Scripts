from ipaddress import ip_address

# Read the comma separated values per line as a 'list'
with open('IP & SR.csv') as ip_sr_csv_sheet:
    ip_sr_pair = ip_sr_csv_sheet.read().splitlines() 

with open('Public_IPs\\All Excluded Public IPs.txt') as excluded_public_ips:
    public_ips = excluded_public_ips.read().splitlines()


with open('CLI Script.txt','w') as CLI_Script:
    CLI_Script.write('configure terminal\n')
    #CREATE NETWORK OBJECTS
    for ip_sr in ip_sr_pair:
        split_ele = ip_sr.split(",")
        try:
            ip, sr = split_ele[0], split_ele[1]
            if ip in public_ips or ip_address(ip).is_private:
                print(ip+' - Not blocked | {}'.format(sr))
                continue
            else:
                CLI_Script.write("object network OBJ_{}\n".format(ip))
                CLI_Script.write("host {}\n".format(ip))
                CLI_Script.write("description Blacklisted {}\n".format(sr))
        except:
            print("'{}' - Invalid IP from {}".format(ip,sr))
            
    CLI_Script.write("exit\n\n")

    #OPEN NETWORK OBJECT GROUP
    CLI_Script.write("object-group network BLOCK_LIST\n")

    #PUSH OBJECTS INTO GROUP
    for ip_sr in ip_sr_pair:
        if ip_sr:
            try:
                ip = ip_sr.split(",")[0]
                if ip in public_ips or ip_address(ip).is_private:
                    continue
                else:
                    CLI_Script.write("network-object object OBJ_{}\n".format(ip))
            except:
                continue

    CLI_Script.write("end\n")
    CLI_Script.write('wr') # Press enter in VTY to write the config

