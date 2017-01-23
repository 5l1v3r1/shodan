#!/usr/bin/env python

import shodan

def shodan_telnet_option():

 try:
  api_object = shodan.Shodan("xxxxxxxxxxxxxxxxx")
  result_object = api_object.count('port:23' , facets = [('telnet.option', 60)])

  for k in result_object['facets']['telnet.option']:
   print '%s --> %s' % (k['value'] , k['count'])

 except shodan.APIError, e:
  print 'Error: %s' % e

shodan_telnet_option(
