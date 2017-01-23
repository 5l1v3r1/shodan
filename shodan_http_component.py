#!/usr/bin/env python

import shodan

def shodan_http_component():

 try:
  api_object = shodan.Shodan("xxxxxxxxxxxxxxxxxxxx")
  result_object = api_object.count('port:20,21,80,81,8080,8081,443', facets = [('http.component', 500)])

  for c in result_object['facets']['http.component']:
   print '%s --> %s' % (c['value'] , c['count'])

 except shodan.APIError, e:
  print 'Error: %s' % e

shodan_http_component()
