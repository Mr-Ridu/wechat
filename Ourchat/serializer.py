from rest_framework import serializers

class room_details_serializer(serializers.Serializer):
    room_name = serializers.CharField(max_length=500)
    reffer_code = serializers.IntegerField()
    username = serializers.CharField(max_length=250)


class messege_details_serializer(serializers.Serializer):
    m_user = serializers.CharField(max_length=250)
    messege = serializers.TextField()
    m_time = serializers.DateTimeField(null=True, blank=True)
    m_room = serializers.CharField(max_length=500)
