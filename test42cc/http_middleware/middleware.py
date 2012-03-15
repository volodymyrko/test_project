from http_middleware.models import HttpRequestStore

class StoreAllHttpRequest(object):
	def process_request(self, request):
		""" Save http request in db
		"""
		path = request.path
		method = request.method
		remote_address = request.META['REMOTE_ADDR']
		http_request = HttpRequestStore(path=path, method=method, remote_address=remote_address)
		http_request.save()
