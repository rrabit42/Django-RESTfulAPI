# Django-RESTfulAPI

### Serializer  
기존 Django를 이용한 웹 개발에서 Django ORM의 Queryset은 Django template로 넘겨지며 HTML로 렌더링되어 Response로 보내지게 됨.  
하지만 JSON으로 데이터를 보내야하는 RESTful API는 HTML로 렌더링 되는 Django template를 사용할 수 없음. 그래서 **Queryset을 Nested한 JSON으로 매핑하는 과정**을 거쳐야 하는데, 이 작업을 Serializer가 하게 된다.
