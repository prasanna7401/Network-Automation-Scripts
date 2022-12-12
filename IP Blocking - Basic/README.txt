DIRECTORY DETAILS:

> IP & SR.csv - A CSV Sheet containing Malicious IP/SR pair
> ASA FW IP Block Scripter.py - This program used the above CSV sheet to generate the config.
> CLI Script.txt - Final configuration that needs to be pasted in the ASA FW CLI

> Public_IPs (Folder)
      >> Excluded Public IP.txt - a list of IPs that should not be blocked (individual IPs)
      >> Subnet_Address.py - This program creates the above txt file from the subnet format-like file
	>> Public IP Subnet - Public IPs to be excluded (in Subnet format)

> Change Rollback
      >> Unblock Script.txt - Use in case of impacts due to blocking an IP | Very less chance

        
NOTE - The Public IPs/Invalid IPs that are not blocked are mentioned in the terminal output and not included in the CLI Script.txt'''
