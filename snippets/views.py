from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Snippet, Tag
from .serializers import (
    SnippetSerializer, SnippetOverviewSerializer, SnippetDetailSerializer,
    TagSerializer,
)


# SNIPPET RELATED VIEWS

class SnippetOverviewAPIView(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetOverviewSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        This function will get the total no.of snippets and the id, title and 
        links to detail, update and delete views.
        '''
        snippets_count = Snippet.objects.count()
        serializer = self.get_serializer(
            self.get_queryset(), many=True, context={'request': request}
        )
        data = {
            'Total no.of snippets': snippets_count,
            'List of snippets': serializer.data
        }

        return Response(data)


class SnippetDetailAPIView(generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetDetailSerializer
    permission_classes = [AllowAny]


class SnippetCreateAPIView(generics.CreateAPIView):
    queryset = Snippet.objects.all()    
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):    
        return Response({'detail': 'Create a new snippet'})


class SnippetUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer 
    permission_classes = [IsAuthenticated]


class SnippetDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        '''
        This function will delete the selected item and will return the 
        list of remaining snippets along with links to their detail, update 
        and delete views.
        '''
        instance = self.get_object()
        try:
            instance.delete()
        except Exception as e:
            return  Response({'detail': str(e)})

        serializer = SnippetOverviewSerializer(
            self.get_queryset(), many=True, context={'request': request}
        )
        return Response(
            {
                'detail': 'Object deleted successfully.',
                'snippet list': serializer.data,
            }
        )

# TAG RELATED VIEWS

class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class TagDetailAPIView(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetOverviewSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        This function will show the details of all the snippets that are 
        associated with the selected tag.
        '''        
        pk = kwargs.get('pk')
        tag_count = Tag.objects.filter(id=pk).count()

        if pk is not None and tag_count > 0:
            snippets = Snippet.objects.filter(tag=pk)
            snippets_count = Snippet.objects.filter(tag=pk).count()
            serializer = self.get_serializer(
                snippets, many=True, context={'request': request}
            )

            data = {
                'Total no.of snippets': snippets_count,
                'List of snippets': serializer.data
            }

            return Response(data)

        return Response({'error': 'Tag not found.'})
