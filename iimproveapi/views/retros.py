from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from iimproveapi.models import Retro, Goal, User
# from rest_framework.decorators import action

class RetroView(ViewSet):
    '''retro View'''
    def retrieve(self, request, pk):
        """ getting single retro data
        """
        retro = Retro.objects.get(pk=pk)

        serializer = RetroSerializer(retro)
        serial_retro = serializer.data
        serial_retro['userId'] = serial_retro.pop('user_id')
        serial_retro['goalId'] = serial_retro.pop('goal_id')
        serial_retro['wentWell'] = serial_retro.pop('went_well')
        serial_retro['toImprove'] = serial_retro.pop('to_improve')
        serial_retro['actionItem'] = serial_retro.pop('action_item')

        return Response(serial_retro)

    def list(self, request):
        '''gets all retros'''
        retro = Retro.objects.all()

        goal_id = request.query_params.get('goalId', None)
        user_id = request.query_params.get('userId', None)
        if goal_id and user_id is not None:
            retro = retro.filter(goal_id = goal_id, user_id = user_id)

        serializer = RetroSerializer(retro, many=True)
        serial_retro = serializer.data
        for retro in serial_retro:
            retro['goalId'] = retro.pop('goal_id')
            retro['userId'] = retro.pop('user_id')
            retro['wentWell'] = retro.pop('went_well')
            retro['toImprove'] = retro.pop('to_improve')
            retro['actionItem'] = retro.pop('action_item')

        return Response(serial_retro)

    def create(self, request):
        '''handels creation of retros'''
        goal_id = request.data['goalId']
        user_id = request.data['userId']

        try:
            Goal.objects.get(id = goal_id)
            User.objects.get(id = user_id)
            retro = Retro.objects.create(
            goal_id = goal_id,
            user_id = user_id,
            went_well = request.data['wentWell'],
            to_improve = request.data['toImprove'],
            action_item = request.data['actionItem'],
            date = request.data['date'],
            status = request.data['status']
            )

            serializer = RetroSerializer(retro)

            return Response(serializer.data)
        except Goal.DoesNotExist as ex:
            return Response({'message': 'Unable to create retro. '
                             + ex.args[0]}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        '''handels delete request for retros'''

        retro = Retro.objects.get(pk=pk)
        retro.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class RetroSerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
        model= Retro
        fields= ('id', 'user_id', 'goal_id','went_well','to_improve','action_item','date','status')
        depth = 2
