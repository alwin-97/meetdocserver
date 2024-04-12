from django.urls import path

from meetdoc import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-audio/', views.upload_audio, name='upload_audio'),
    path('upload-audio-list/', views.upload_audio_list, name='upload_audio_list'),
    path('audio-transcript-gen/<int:audio_id>', views.audio_transcript_gen, name='audio_transcript_gen'),
    path('audio-transcript-fetch/<int:audio_id>', views.audio_transcript_fetch, name='audio_transcript_fetch'),
    path('audio-summary-gen/<int:audio_id>', views.audio_summary_gen, name='audio_summary_gen'),
    path('audio-summary-fetch/<int:audio_id>', views.audio_summary_fetch, name='audio_summary_fetch'),
    path('audio-mom-gen/<int:audio_id>', views.audio_mom_gen, name='audio_mom_gen'),
    path('audio-mom-fetch/<int:audio_id>', views.audio_mom_fetch, name='audio_mom_fetch'),
    path('update-summary/<int:audio_id>', views.update_summary, name='update_summary'),
    path('update-transcript/<int:audio_id>', views.update_transcript, name='update_transcript'),
    path('update-mom/<int:audio_id>', views.update_mom, name='update_mom'),
    path('remove-audio/<int:audio_id>', views.delete_audio, name='delete_audio'),
    path('share-meeting-report/<int:audio_id>', views.share_meeting_report, name='share_meeting_report'),

    #     admin users view
    path('admin-dashboard', views.meetdoc_admin, name='admin-dashboard'),
    path('list-users', views.list_users, name='list-users'),
]
