from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # 타입이 없는 ReadOnlyField는 직렬화에 사용되었을 땐 언제나 읽기 전용이므로, 모델의 인스턴스를 업데이트할 때는 사용할 수 없음. CharField(read_only=True)도 이와 같은 기능을 수행
    # 이 필드에는 조금 재미있는 면이 있어욥! source 인자로는 특정 필드를 지정할 수 있음. 여기에는 직렬화된 인스턴스의 속성 뿐만 아니라 위의 코드에서처럼 마침표 표기 방식을 통해 특정 속성을 탐색할 수도 있음. 마치 Django의 템플릿 언어와 비슷
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html') # 이 필드는 url 필드와 같은 타입이며, 'snippet-detail' url 패턴 대신 'snippet-highlight' url 패턴을 가리킴

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # HyperlinkedModelSerializer를 사용하면
    # pk 필드는 기본 요소가 아님
    # HyperlinkedIdentityField를 사용하는 url 필드가 포함되어 있음
    # 관계는 PrimaryKeyRelatedField 대신 HyperlinkedRelatedField를 사용
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')