from django.http import HttpResponse


def demo_middleware(get_response):
    print("one time initialization!")

    def fun_middleware(request):
        print("this is before view calling!")
        response = get_response(request)
        print("after view calling!")
        return response

    return fun_middleware


class demo_middleware_cls:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("this is before view calling! class")
        response = self.get_response(request)
        print("after view calling! class")
        return response


class first_middleware_cls:
    def __init__(self, get_response):
        self.get_response = get_response
        print("onetime first middleware initialization!")

    def __call__(self, request):
        print("this is before view calling of first middleware")
        response = self.get_response(request)
        # response = HttpResponse("response form first middleware")
        print("this is after view calling of first middleware")
        return response


class second_middleware_cls:
    def __init__(self, get_response):
        self.get_response = get_response
        print("onetime second middleware initialization!")

    def __call__(self, request):
        print("this is before view calling of second middleware")
        response = self.get_response(request)
        # response = HttpResponse("response form second middleware")
        print("this is after view calling of second middleware")
        return response


class third_middleware_cls:
    def __init__(self, get_response):
        self.get_response = get_response
        print("onetime third middleware initialization!")

    def __call__(self, request):
        print("this is before view calling of third middleware")
        response = self.get_response(request)
        # response = HttpResponse("response form third middleware")
        print("this is after view calling of third middleware")
        return response
