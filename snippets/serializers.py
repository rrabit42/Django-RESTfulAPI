from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    # 타입이 없는 ReadOnlyField는 직렬화에 사용되었을 땐 언제나 읽기 전용이므로, 모델의 인스턴스를 업데이트할 때는 사용할 수 없음. CharField(read_only=True)도 이와 같은 기능을 수행
    # 이 필드에는 조금 재미있는 면이 있어욥! source 인자로는 특정 필드를 지정할 수 있음. 여기에는 직렬화된 인스턴스의 속성 뿐만 아니라 위의 코드에서처럼 마침표 표기 방식을 통해 특정 속성을 탐색할 수도 있음. 마치 Django의 템플릿 언어와 비슷
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        field = ('id', 'username', 'snippets')