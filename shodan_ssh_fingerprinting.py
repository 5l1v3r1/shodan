#!/usr/bin/env python

import shodan

def ssh_fingerprint():

 try:
  api = shodan.Shodan("xxxxxxxxxxxxxxxxxx")
  results_obj = api.count('port:22' , facets = [('ssh.fingerprint' , 1000)])

  for facet in results_obj['facets']['ssh.fingerprint']:
   print '%s --> %s' % (facet['value'] , facet['count'])

 except shodan.APIError, e:
  print 'Error: %s' % e

ssh_fingerprint()
