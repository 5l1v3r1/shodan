#!/usr/bin/env python

import shodan
import sys

if len(sys.argv) < 2:
 print "Usage python host_shodan.py <ipaddress>"
 exit()

def shodan_host():

 api_object = shodan.Shodan("xxxxxxxxxxxxx")
 host = api_object.host(sys.argv[1])

 print """
           IP: %s
           Host: %s
           Organization: %s
           Operating System: %s

 """ % (host['ip_str'],host.get('hostnames'),host.get('org'),host.get('os'))

 for item in host['data']:
  print """ Port: %s
            Banner: %s """ % (item['port'] , item['data'])

shodan_host()
