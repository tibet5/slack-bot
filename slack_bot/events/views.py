from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from slack_bot.settings import SLACK_VERIFICATION_TOKEN


class Events(APIView):
    def post(self, request, *args, **kwargs):
        slack_message = request.data

        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


# Create your views here.
