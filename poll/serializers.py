from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'name')

class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'name', 'desc', 'choice_set')
