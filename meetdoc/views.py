from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({'message': 'Welcome to meetdoc'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def upload_audio(request):
    return Response({'message': 'Upload Audio File'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def upload_audio_list(request):
    return Response({'message': 'Upload Audio List'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def audio_transcript_gen(request, audio_id):
    return Response({'message': 'API to convert the audio to transcript'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def audio_transcript_fetch(request, audio_id):
    return Response({'message': 'API to fetch the transcript'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def audio_summary_gen(request, audio_id):
    return Response({'message': 'API to summarize the audio'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def audio_summary_fetch(request, audio_id):
    return Response({'message': 'API to fetch the summary of the audio'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def audio_mom_gen(request, audio_id):
    return Response({'message': 'API to convert the audio to mom'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def audio_mom_fetch(request, audio_id):
    return Response({'message': 'API to fetch the mom of the audio'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_summary(request, audio_id):
    return Response({'message': 'API to update the summary of the audio'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_transcript(request, audio_id):
    return Response({'message': 'API to update the transcript of the audio'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_mom(request, audio_id):
    return Response({'message': 'API to update the mom of the audio'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_audio(request, audio_id):
    return Response({'message': 'API to delete the audio'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def share_meeting_report(request, audio_id):
    return Response({'message': 'API to share meeting report'}, status=status.HTTP_200_OK)


# ADMIN USER
@api_view(['GET'])
def meetdoc_admin(request):
    return Response({'message': 'API meetdoc admin'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_users(request):
    return Response({'message': 'API meetdoc admin'}, status=status.HTTP_200_OK)
