from django.contrib.auth.models import User, Group
from rest_framework import serializers


# HyperlinkedModelSerializer?
# A type of 'ModelSerializer' that uses hyperlinked relationships instead of primay key relationships.
# A 'url' field is included instead of the 'id' field.
# Relationships to other instances are hyperlinks, instead of primary keys.
# ex) student 모델이 class 모델은 foreign key로 참조하는 경우
# ModelSerializer로 시리얼라이즈하면 {"name":"홍길동", "age":17, "class": 1}
# HyperlinkedModelSerializer로 시리얼라이즈하면 {"name": 홍길동", "age":17, "class", "http://.../class/1"}
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']