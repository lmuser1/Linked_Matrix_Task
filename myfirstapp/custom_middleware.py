import logging

class MyCustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        logging.basicConfig(filename='example.log', format= 'Ip Address is: %(message)s and the time is: %(asctime)s', encoding='utf-8', level=logging.INFO)
        logging.info(request.META['REMOTE_ADDR'])
        return response