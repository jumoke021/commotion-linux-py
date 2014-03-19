#commotion.py
import re
# Validation for parameters channel,ssid, bssid, ip, ipgenerate, netmask, and dns

# Assumes the following ... 
             # strings ssid, bssid, ip, netmask, dns
             # boolean = ipgenerate ( just for boolean values) 
             # string channel but limited to values same as in commotion - lua helper

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
            val = re.match(r"(\w+).net",profile['ssid'])
            if not val:
                return False
        elif param =='bssid':
            print 'Checkign bssid'
            m_val = re.split(':(?=[^:])',profile[param]) # split params by ':'
            val= re.match('(\w+)',''.join(m_val)) # check if bssid only contains alphanumerical values
            if not val:
                return False
        else:
            print 'Checking ip,netmask,dns'
            m_val = re.split('.(?=[^.])',profile[param]) # split params by '.'             
            val = re.match('[^0-9]',''.join(m_val)) # Check if alpha characters exist if do return false
            if val :
                return False
    if param == 'ipgenerate':
        print 'checking ipgenerate'
        if not bool(profile[param]):
            return False
    if param == 'channel':
        if not int(profile['channel']) in channels:
            print 'Checking channel'
            return False
    
