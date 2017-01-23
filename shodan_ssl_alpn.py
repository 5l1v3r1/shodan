#!/usr/bin/env python

import shodan

def shodan_ssl_alpn():

 try:
  api_object = shodan.Shodan("xxxxxxxxxxxxxxxxxxxx")
  result_object = api_object.count('port:443,8443,8080' , facets = [('ssl.alpn', 60)])

  for n in result_object['facets']['ssl.alpn']:
   print '%s --> %s' % (n['value'] , n['count'])

 except shodan.APIError, e:
  print 'Error: %s' % e

shodan_ssl_alpn()
