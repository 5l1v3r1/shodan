#!/usr/bin/env python

import sys
import shodan

if len(sys.argv) < 2:
 print "Usage : python shodan_search.py <search string>"
 print "Example: python shodan_search.py <fingerprinting> or <string>"
 exit()

def shodan_search():

 try:
  api_object = shodan.Shodan("xxxxxxxxxxxxxxxxxxxxxx")
  request_object = " ".join(sys.argv[1:])
  result_object = api_object.search(request_object)
  print 'Results: %s' % result_object['total']

  for j in result_object['matches']:
   print 'IP: %s' % j[('ip')]
   print 'IP: %s' % j[('ip_str')]
   print 'Port: %s' % j[('port')]
   print 'Host: %s' % j[('hostnames')]
   print 'Provider: %s' % j[('isp')]
   print j[('data')]
   print ''

 except Exception as e:
  print 'Error: %s' % e
  exit()

shodan_search()
