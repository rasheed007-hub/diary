from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework import response

from .serializers import DiarySerialzer
from .models import Diary
# Create your views here.

class DiaryList(APIView):
    def post(self, request):
        try:
            serializer = DiarySerialzer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return response.Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self,request):
            try:
                diary = Diary.objects.all()
                serializer = DiarySerialzer(diary,many=True)
                return response.Response(serializer.data,status=status.HTTP_200_OK)
            except Exception as e:
                return response.Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class DiaryDetailView(APIView):
    def get(self,request, id):
        try:
            diary = Diary.objects.get(id=id)
            serializer = DiarySerialzer(diary)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({"Message" : str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            diary = Diary.objects.get(id=id)
            serializer = DiarySerialzer(diary, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return response.Response({"Message" : str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id): 
        try:
            todo = Diary.objects.get(id=id)
            todo.delete()
            return response.Response({"Message" : "Todo deleted successfuly"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return response.Response({"Message" : str(e)}, status=status.HTTP_404_NOT_FOUND)