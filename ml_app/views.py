# ml_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def parse_resume_view(request, candidate_id):
    if request.method == 'GET':

        # Use candidate_id to fetch data from the database
        # Replace the following line with your actual database query logic
        candidate_data = {'id': candidate_id}

        return JsonResponse(candidate_data)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})
