#!/usr/bin/env python
# Simple Admin Finder ( https://pasoendanbrigadez.ml )
import requests

print "Masukkan path file : ",
filenya = raw_input()
dir = open(filenya,'r')

print "Masukkan url ( gunakan http:// atau https:// ) : ",
uerel = raw_input()

for line in dir.read().split('\n'):
	r = requests.get(uerel + "/" + line,
	    headers = {'User-agent' : 'Internet Explorer/2.0'})
	print "-"*70
	print "URL : " + r.url
	if(r.status_code == 200):
		print "STATUS : \33[92m" + str(r.status_code) + "\33[0m"
	else:
		print "STATUS : " + str(r.status_code)
	print "-"*70


dir.close()
