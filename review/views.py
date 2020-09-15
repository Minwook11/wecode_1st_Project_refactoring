from django.views import View
from django.http import JsonResponse

class ReviewView(View):
    def get(self, request):
        return JsonResponse({'message' : 'Review View GET'}, status = 200)

class ReviewDetailView(View):
    def get(self, request):
        return JsonResponse({'message' : 'Review Detail View GET'}, status = 200)
