from django.http import HttpResponse, HttpResponseRedirect


def home(request):

    response = HttpResponse(content_type='text/html')
    response.content = '<h1>Hello World!!!</h1>'

    print(response.status_code)

    response.status_code = 200

    return response


def home_page(request):
    return HttpResponse('<h4>You was redirected at the Page</h4>')


def redirect_to_page(request):

    return HttpResponseRedirect('/page')
