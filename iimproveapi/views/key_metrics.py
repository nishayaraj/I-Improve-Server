from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from iimproveapi.models import KeyMetrics, Goal
# from rest_framework.decorators import action

class KeyMetricsView(ViewSet):
    '''key metrics View'''
    def retrieve(self, request, pk):
        """ getting my goal data by id
        """
        key_metrics = KeyMetrics.objects.get(pk=pk)

        serializer = KeyMetricsSerializer(key_metrics)
        serial_key_metrics = serializer.data
        serial_key_metrics['goalId'] = serial_key_metrics.pop('goal_id')

        return Response(serial_key_metrics)

    def list(self, request):
        '''handles list by goal id'''
        goal_id = request.GET.get("goalId")
        key_metrics = KeyMetrics.objects.filter(goal_id=goal_id)

        serialized_key_metrics = (KeyMetricsSerializer(key_metrics, many=True)).data
        for key_metrics in serialized_key_metrics:
            key_metrics['goalId'] = key_metrics.pop('goal_id')

        return Response(serialized_key_metrics)

    def create(self, request):
        '''handels creation of key metrics'''
        goal_id = request.data['goalId']

        try:
            Goal.objects.get(id = goal_id)
            key_metrics = KeyMetrics.objects.create(
            goal_id = goal_id,
            title = request.data['title'],
            status = request.data['status']
            )

            serializer = KeyMetricsSerializer(key_metrics)

            return Response(serializer.data)
        except Goal.DoesNotExist as ex:
            return Response({'message': 'Unable to create key metric. '
                             + ex.args[0]}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk):
        """Handle PUT requests for keyMetrics

        Returns:
        Response -- Empty body with 204 status code
        """

        key_metrics = KeyMetrics.objects.get(pk=pk)
        key_metrics.title = request.data['title']
        key_metrics.status = request.data['status']

        key_metrics.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        '''handels delete request for key metrics'''

        key_metrics = KeyMetrics.objects.get(pk=pk)
        key_metrics.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class KeyMetricsSerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
        model= KeyMetrics
        fields= ('id', 'title', 'status', 'goal_id')
        depth = 1
