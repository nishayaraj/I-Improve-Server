from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from iimproveapi.models import Goal, GoalTag, Tag, KeyMetrics


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
                    tag_on_goal = Tag.objects.get(id=goal_tag.tag_id)
                    tags_on_goal.append(
                        {'id': tag_on_goal.id, 'title': tag_on_goal.title})
                except:
                    pass

            serial_goal['tags'] = tags_on_goal

            return Response(serial_goal)
        except Goal.DoesNotExist as ex:
            return Response({'message': 'Unable to fetch goal data. '
                             + ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        '''get all goals, tags & key metrics by user id'''
        user_id = request.GET.get("userId")
        goals_user_id = Goal.objects.filter(user_id=user_id)

        serialized_goals_user_id = (GoalSerializer(goals_user_id, many=True)).data

        for goal in serialized_goals_user_id:
            goal['userId'] = goal.pop('user_id')

            # fetching tags for the goal
            filtered_goal_tags = GoalTag.objects.filter(goal_id=goal['id'])
            tags_on_goal = []
            for goal_tag in filtered_goal_tags:
                tag_on_goal = Tag.objects.get(id=goal_tag.tag_id)
                tags_on_goal.append({'id': tag_on_goal.id, 'title': tag_on_goal.title})
            goal['tags'] = tags_on_goal

            # fetching key metrics for the goal
            filtered_goal_key_metrics = KeyMetrics.objects.filter(goal_id=goal['id'])
            serialized_goal_key_metrics = (KeyMetricsSerializer(filtered_goal_key_metrics,
                                                                many=True)).data
            for key_metric in serialized_goal_key_metrics:
                key_metric['goalId'] = key_metric.pop('goal_id')
            goal['keyMetrics'] = serialized_goal_key_metrics

        return Response(serialized_goals_user_id)

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
        model = Goal
        fields = ('id', 'user_id', 'title', 'due')
        depth = 1

class KeyMetricsSerializer(serializers.ModelSerializer):
    '''JSON Serializer'''
    class Meta:
        model= KeyMetrics
        fields= ('id', 'title', 'status', 'goal_id')
        depth = 1
