from django.shortcuts import redirect


class Identification:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Do something before the view is called
        if not request.COOKIES.get('token'):
            return redirect('signin')

        response = self.get_response(request)

        # Do something after the view is called

        return response