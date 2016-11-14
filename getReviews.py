'''
@desc : This script allows anyone to fetch reviews for "any" app available on playstore.
		For educational purpose only. 
		Script is in its initial stage, so expect bugs. 
@author : 5h1vang
'''

import json, sys, re, os
import requests
import config

def collectReview(output, pageNum):
	filename = config.pkg_name + "_reviews.html"
	f = open(filename, 'a')
	#f.write(req_output) #if req_output is stored then unicode error is being raised.. 
	f.write(output)
	f.close()
	print "Review saved for page number ", pageNum


def requestReview():
	response = requests.post(config.url, headers=config.headers, data=config.payload)
	if response.status_code != 200 :
		print "Failed to get 200-OK."
		sys.exit(0)
	print response.headers['content-type']
	
	print "----------------->", response.encoding
	if len(response.content) < 100:
		print "No reviews available for particular App."
		sys.exit(0)

	pageNum = 1
	try:
		while len(response.content) > 100:
			output = response.text.encode('ascii','ignore')
			#collectReview(response.text)
			collectReview(output, pageNum)
			new_payload = {'reviewType':0, 'pageNum':pageNum, 'id':config.pkg_name, 'reviewSortOrder':2, 'xhr':1}
			response = requests.post(config.url, headers=config.headers, data=new_payload)
			pageNum = pageNum + 1 
	except Exception as e:
		print "Oops...Exception generated while fetching reviews.\n"
		print e

	#call decodeFile here
	print "Decoding file...... Please wait!"
	decodeFile()

def decodeFile():
	import codecs
	encoded_file = config.pkg_name + "_reviews.html"
	f_read = codecs.open(encoded_file, encoding='ascii')
	data = ""
	for line in f_read:
	    #print line.decode('unicode-escape')
	    data = data + line.decode('unicode-escape')

	decoded_file = config.pkg_name + "_decoded.html"
	f_write = open(decoded_file, 'w')
	f_write.write(data)
	f_write.close()
	os.remove(encoded_file)
	print "Reviews stored in ", decoded_file


if __name__ == '__main__':
	requestReview()