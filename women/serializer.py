import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women

class WomenModel:
    def __init__(self,title,content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = "__all__"





    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(read_only=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.title = validated_data.get('content', instance.title)
    #     instance.title = validated_data.get('time_update', instance.title)
    #     instance.title = validated_data.get('is_published', instance.title)
    #     instance.title = validated_data.get('cat_id', instance.title)
    #     instance.save()
    #     return instance




# def encode():
#     model = WomenModel('Дженни Ким','Content: Дженни Ким')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json,type(json),sep='\n')
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Дженни Ким","content":"Content: Дженни Ким"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

