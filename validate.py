#!/usr/bin/env python

# Validation for parameters channel,ssid, bssid, ip, ipgenerate, netmask, and dns

# Assumes the following ... 
             # strings ssid, bssid, ip, netmask, dns
             # boolean = ipgenerate ( just for boolean values) 
             # string channel but limited to values same as in commotion - lua helper

import re
profile = dict();
profile['bssid']='02:CA:FF:EE:BA:BE'
profile['ssid']='commotion.net'
profile['ip']='5.0.0.0'
profile['netmask']='255.0.0.0'
profile['dns']='255.0.0.0'
profile['ipgenerate']= 'True'
profile['channel']='255.0.0.0'


def validate(param, profile):
    channels = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,36,40,44,48,149,153,157,161,165}
    
    if param in {'ssid','bssid','ip','netmask','dns'}:
        print param
        if param =='ssid':
            print 'Checking ssid'
            val = re.findall(r"[^\w]",profile['ssid']) # check for non-alphanumeric characters
            if not val: # if none found 
                ssid_len=len(profile['ssid'])
                if ssid_len <= 32:
                    return True
                else:
                    return False
            else:
                return False
        elif param =='bssid':
            print 'Checking bssid'
            val= re.findall('[a-fA-F0-9][a-fA-F0-9]',profile[param]) # check if bssid only contains hexadecimal values
            if val and len(val) == 6:
                if not val[0] == '02': # check that first byte is '02'
                    return False 
                else:
                    return True
            else:
                return False 
                
        else:
            print 'Checking ip,netmask,dns'             
            val = re.split(r"[^.]",profile[param]) # Check if alpha characters exist if do return false
            if val: 
                for octet in val:
                    if not int(octet)<= 255:
                        return False
                        break
                    if octet == val[-1]:
                        return True
            else:
                return False
## Removed ipgenerate check because its values are checked outside this function
##    if param == 'ipgenerate':
##        print 'checking ipgenerate'
##        if not bool(profile[param]):
##            return False
##        else:
##            return True
    if param == 'channel':
        print 'Checking channel'
        if not int(profile['channel']) in channels:
            return False
        else:
            return True
