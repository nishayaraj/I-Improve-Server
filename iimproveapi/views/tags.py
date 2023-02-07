from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from iimproveapi.models import Tag, User

class TagsView(ViewSet):
    """iimproveapi tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag type
        Returns:
            Response -- JSON serialized tag type
        """
        try:
            tag = Tag.objects.get(pk=pk)

            serializer = TagSerializer(tag)
            serial_tag = serializer.data
            serial_tag['userId'] = serial_tag.pop('user_id')
            return Response(serial_tag)

        except Tag.DoesNotExist as ex:
            return Response({'message': 'Unable to fetch tag data. '
                             + ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """get my tags"""
        try:
            user_id = request.GET.get("userId")
            tags = Tag.objects.filter(user_id=user_id).values()
            serializer = TagSerializer(tags, many=True)
            serial_tag = serializer.data
            for tag in serial_tag:
                tag['userId'] = tag.pop('user_id')
            return Response(serial_tag)
        except Tag.DoesNotExist as ex:
            return Response({'message': 'Unable to get my tag data. '
                             + ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        '''handels creation of my tags'''
        user_id = request.data['userId']

        try:
            User.objects.get(id = user_id)
            tag = Tag.objects.create(
            title = request.data['title'],
            user_id = user_id
            )

            serializer = TagSerializer(tag)

            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': 'Unable to create tag. '
                             + ex.args[0]}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk):
        """Handle Delete
        """
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags
    """
    class Meta:
        model = Tag
        fields = ('id', 'title', 'user_id')
