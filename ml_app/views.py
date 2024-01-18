from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from user.models import Candidate
from .utils import DepartmentWiseAlignment  # Assuming you have a utility function named DepartmentWiseAlignment

class ParseResumeView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        response = {}
        candidates = Candidate.objects.all()

        for candidate in candidates:
            resume = candidate.resume
            alignment_percentage = DepartmentWiseAlignment(resume)
            length = min(len(alignment_percentage.items()), 3)
            candidate_response = dict(sorted(alignment_percentage.items(), key=lambda item: item[1], reverse=True)[:length])
            response[candidate.id] = candidate_response

        return Response(response, status=status.HTTP_200_OK)