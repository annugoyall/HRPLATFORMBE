# ml_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import Candidate
from .utils import ParseResume, GetKeywords, DepartmentWiseAlignment

@csrf_exempt
def parse_resume_view(request, candidate_id):
    if request.method == 'GET':
        candidate = Candidate.objects.get(id=candidate_id)
        if candidate.exist():
            resume = candidate.resume

        parsed_resume = ParseResume(resume)
        get_keywords = GetKeywords(parsed_resume)
        return DepartmentWiseAlignment(get_keywords)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'})
