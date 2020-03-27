from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url


import stripe
stripe.api_key = "sk_test_FQfSktUAeYgQ51Jqqc7VJ9sp00aUrZajyb"

STRIPE_PUB_KEY = 'pk_test_jbYKNdGc06kkYEd5eXIXeQdu00yxQPkVex'


def payment_method_view(request):
    # next_url =
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})


def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        print(request.POST)
        return JsonResponse({"message": "Done"})
    return HttpResponse("error", status_code=401)
