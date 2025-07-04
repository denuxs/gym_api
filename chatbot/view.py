from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from openai import OpenAI

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from django.conf import settings


class ParameterSerializer(serializers.Serializer):
    query = serializers.CharField(
        required=True,
    )


SYSTEM_PROMPT = """
You are a professional fitness coach specializing in gym routines, exercise techniques, and fitness advice. Provide accurate, safe, and practical answers related to gym workouts, strength training, cardio, nutrition for fitness, and injury prevention. Always prioritize user safety and recommend consulting a professional for personalized advice. If a question is unclear or outside the scope of fitness, politely clarify or redirect to gym-related topics.
"""


class ChatbotView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ParameterSerializer

    @swagger_auto_schema(
        request_body=ParameterSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            user_query = serializer.validated_data["query"]

            try:

                client = OpenAI(api_key=settings.OPENAI_API_KEY)

                response = client.responses.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-4",  # Puedes usar 'gpt-4', 'gpt-3.5-turbo', etc.
                    # model="gpt-4.1",
                    instructions=SYSTEM_PROMPT,
                    input=[
                        {"role": "user", "content": user_query},
                    ],
                )

                content = response.output_text
                print(content)

                return Response({"content": content})

            except Exception as e:
                print(
                    f"Error: Could not connect to the ChatGPT API. Please check your API key and internet connection. Details: {str(e)}"
                )
                return Response({"error": "Could not connect to the ChatGPT API."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
