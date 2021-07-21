from django.http import HttpResponse
def FirstMiddleware(get_response):
    print("One time Intitalization")
    def first_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return first_function

class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Yha ka code ek baar chalega")
    
    def __call__(self, request):
        print("View se pehle ka code")
        response = self.get_response(request)
        print("View k baad ka code")
        return response
    
    def process_view(request,*args, **kwargs):
        print("Yeh function view k chalne se pehle chlta h")
        return HttpResponse("Hello Keshav !")