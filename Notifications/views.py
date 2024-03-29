from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
def notification_list(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
