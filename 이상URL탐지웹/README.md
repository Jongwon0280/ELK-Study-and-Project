### 아키텍처 및 디렉토리 구조

![Untitled](https://user-images.githubusercontent.com/56438131/223625883-e49bc176-0e52-4987-a9c8-c8f945f1bd9e.png)

**서버1**

웹에서 사용자에게 입력을 받아야하므로, 파이썬 웹서버 프레임워크 Django와 Flask 중에서 비교적 간단히 구현이 가능한 Flask를 선택했다.

사용자의 입력(url)을 불러오고 그값을 파이썬을 통해 파싱한 후 특징을 추출한 후 예측을 하며 예측값은 사용자 화면에 출력되고, 로그생성을 수행하여 logstash에서 opensearch로 forwarding한다.   

**서버2**

logstash에서 forwarding한 값을 opensearch로 받아온 후 open-dashboard를 연동하여 실시간으로 로그를 수집할 수 있는 서버이다.