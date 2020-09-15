from django.views import View
from django.http import JsonResponse

class AllTeaView(View):
    def get(self, request):
        return JsonResponse({'message' : 'All Tea View GET'}, status = 200)

class RefineView(View):
    def get(self, request):
        return JsonResponse({'message' : 'Refine View GET'}, status = 200)

class TeaDetailView(View):
    def get(self, request):
        return JsonResponse({'message' : 'Tea Detail View GET'}, status = 200)
