from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer, JobCreateSerializer
from .tasks import schedule_job

class JobViewSet(viewsets.ViewSet):
    def list(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = JobCreateSerializer(data=request.data)
        if serializer.is_valid():
            job = serializer.save()
            schedule_job(job)  # Schedule the job
            return Response(JobSerializer(job).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)