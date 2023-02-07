from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from iimproveapi.models import Tag

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
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all tag types
        Returns:
            Response -- JSON serialized list of tag types
        """

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
        Response -- JSON serialized tag instance
        """
        tag = Tag.objects.create(
          title=request.data["title"]
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)

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
        fields = ('id', 'title')
