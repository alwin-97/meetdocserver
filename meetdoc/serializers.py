from rest_framework import serializers

from meetdoc.models import upload_audio, audio_summary, audio_transcript, audio_mom


class audioSerializer(serializers.ModelSerializer):
    class Meta:
        model = upload_audio
        fields = ['filename', 'upload_by']


class audioSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_summary
        fields = ['audio', 'summary']


class audioTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_transcript
        fields = ['audio', 'transcript']


class audioMoMSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_mom
        fields = ['audio', 'mom']
