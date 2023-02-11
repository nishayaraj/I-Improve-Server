from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from iimproveapi.models import Goal, GoalTag

class GoalsView(ViewSet):
    """Goal View

        Returns:
            Response -- JSON serialized goal data
        """

    def retrieve(self, request, pk):
        """ getting goal by id
        """
        try:
            goal = Goal.objects.get(pk=pk)

            serializer = GoalSerializer(goal)
            serial_goal = serializer.data
            serial_goal['userId'] = serial_goal.pop('user_id')

            filtered_goal_tags = GoalTag.objects.filter(goal_id=goal.id)
            tags_on_goal = []

            for goal_tag in filtered_goal_tags:
                try:
                    tag_on_goal = Goal.objects.get(id=goal_tag.tag_id)
                    tags_on_goal.append({'id': tag_on_goal.id, 'title': tag_on_goal.title})
                except:
                    pass

            serial_goal['tags'] = tags_on_goal

            return Response(serial_goal)
        except Goal.DoesNotExist as ex:
            return Response({'message': 'Unable to fetch goal data. '
                             + ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        '''Delete request for goal'''
        try:
            goal = Goal.objects.get(pk=pk)
            goal.delete()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Goal.DoesNotExist as ex:
            return Response({'message': 'Unable to goal. '
                             + ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class GoalSerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
        model= Goal
        fields= ('id', 'user_id','title','due')
        depth = 1
