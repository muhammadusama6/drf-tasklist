from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from tasklist.models import tasklist
from tasklist.serializers import tasklistSerializer


class TasklistViewSet(viewsets.ModelViewSet):
    model = tasklist
    queryset = model.objects.all()
    serializer_class = tasklistSerializer
    # authentication_classes = [JSONWebTokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        data = tasklist.objects.all()
        serializer = tasklistSerializer(data, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        task = tasklist.objects.create(
            task_name=request.data['task_name'],
            task_id=request.data['task_id'],
            is_checked=request.data['is_checked']
        )
        serialized_task = tasklistSerializer(instance=task)
        response = {
            'task': serialized_task.data
        }
        return Response(data=response)

    def delete(self, request, pk=None):
        task = self.get_object(pk)
        task.delete()
        response = {
            'message': 'Task deleted successfully'
        }
        return Response(data=response)