# ml_app/views.py
from django.views.decorators.csrf import csrf_exempt
from user.models import Candidate
from .utils import ParseResume, GetKeywords, DepartmentWiseAlignment
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
def parse_resume_view(request, candidate_id):
    if request.method == 'GET':
        response = []
        candidates = Candidate.objects.all()
        for candidate in candidates:
            resume = candidate.resume
            parsed_resume = ParseResume(resume)
            get_keywords = GetKeywords(parsed_resume)
            alignment_percentage = DepartmentWiseAlignment(get_keywords)
            alignment_percentage.sort(reverse=True)
            response.append(alignment_percentage[:3])
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Only GET requests are allowed'}, status=status.HTTP_400_BAD_REQUEST)
