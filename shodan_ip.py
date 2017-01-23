#!/usr/bin/env python

import shodan
import sys

if len(sys.argv) < 2:
 print "Usage: python shodan_ip.py <search string>"
 print "Exemple: python shodan_ip.py <fingerprinting> or <string>"
 exit()

def shodan_ips():

 try:
  api_object = shodan.Shodan("xxxxxxxxxxxxxxxxxx")
  request_object = " ".join(sys.argv[1:])
  result_object = api_object.search(request_object)

  for service in result_object['matches']:
   print service[('ip')]
   print service[('ip_str')]
   print service[('port')]
   print service[('hostnames')]
   print service[('org')]
   print service[('isp')]

 except Exception as e:
  print "Error: %s" % e
  exit()

shodan_ips()
