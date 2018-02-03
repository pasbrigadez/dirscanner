#!/usr/bin/env python
# Simple Admin Finder ( https://pasoendanbrigadez.ml )
import requests

print "Masukkan path file : ",
filenya = raw_input()
dir = open(filenya,'r')

print "Masukkan url ( gunakan http:// atau https:// ) : ",
uerel = raw_input() 
y = 0
a = open('ditemukan.txt','w')
for line in dir.read().split('\n'):
	r = requests.get(uerel + "/" + line,
	    headers = {'User-agent' : 'Internet Explorer/2.0'})
	print "-"*70
	def test():
		if(r.status_code == 200):
			z = r.url
			a.write(z+"\n")
	if(r.status_code == 200):
		print r.url
		print "STATUS : \33[92m" + str(r.status_code) + "\33[0m"
		y+=1
	else:
		print r.url
		print "STATUS : " + str(r.status_code)
	print "-"*70
	test()
print "Dir yang ditemukan ada : \33[92m%s" % y
a.close()
dir.close()
