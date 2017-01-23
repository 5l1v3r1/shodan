#!/usr/bin/env python

import shodan

def shodan_ssl_cert():

 try:
  api_object = shodan.Shodan("xxxxxxxxxxxxxxxxxxxxxxxxxx")
  result_object = api_object.count('port:443,8443' , facets=[('ssl.cert.serial', 60)])

  for z in result_object['facets']['ssl.cert.serial']:
   print '%s --> %s' % (z['value'] , z['count'])

 except shodan.APIError, e:
  print 'Error: %s' % e

shodan_ssl_cert()
