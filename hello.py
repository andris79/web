import os
import sys
def app (environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/plain')]
	start_response(status, response_headers)
	resp = environ['QUERY_STRING'].split("&")
	resp = [item+"\r\n" for item in resp]
#	resp = str(resp)
#	return [resp.encode('utf-8')]
	return "\n".join(resp)

#def app(environ, start_response):
#	status = '200 OK'
#	headers = [
#	('Content-Type', 'text/plain')
#	]
#	body = 'Hello, world!'
#	start_response(status, headers )
#	return [ body ]

