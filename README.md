# Linked_Matrix_Task

## First task
I have implemented the logging module of python to get the IP and Time of user who sends request to our app,
it is done in seperate middleware and middleware was added in settings.py in middleware section
```
MIDDLEWARE = [
    ........
    'myfirstapp.custom_middleware.MyCustomMiddleware',
    ........
]
```

the code for middleware is in custom_middleware.py
```
import logging
class MyCustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response    
    def __call__(self, request):
        response = self.get_response(request)
        logging.basicConfig(filename='example.log', format= 'Ip Address is: %(message)s and the time is: %(asctime)s', encoding='utf-8', level=logging.INFO)
        logging.info(request.META['REMOTE_ADDR'])
        return response
 ```
 
 the log file is made named "example.log"
 
 ![This is an image](/assets/images/electrocat.png)
