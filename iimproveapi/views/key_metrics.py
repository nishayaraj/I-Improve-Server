'''Comments module for request handeling'''

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
        '''handels list by goal id'''
        key_metrics = KeyMetrics.objects.all()

        goal_id = request.query_params.get('goalId', None)
        if goal_id is not None:
            key_metrics = key_metrics.filter(goal_id = goal_id)

        serializer = KeyMetricsSerializer(key_metrics, many=True)
        serial_key_metrics = serializer.data
        for key_metrics in serial_key_metrics:
            key_metrics['goalId'] = key_metrics.pop('goal_id')

        return Response(serial_key_metrics)


    # def create(self, request):
    #     '''handels creation of key metrics by goalId'''
    #     goal_id = Goal.objects.get(pk=request.data['goalId'])

    #     key_metrics = KeyMetrics.objects.create(
    #       goal_id = goal_id,
    #       title = request.data['title'],
    #       status = request.data['status']
    #     )

    #     serializer = KeyMetricsSerializer(key_metrics)

    #     return Response(serializer.data)

    def create(self, request):
        '''handels creation of my journals'''
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
