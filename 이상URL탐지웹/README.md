### Description

<br>

로그데이터 실시간 수집 및 분석 시각화 솔루션인 ELK Stack을 활용한 이상 URL 탐지 웹입니다.

> 데이터셋 
> https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset

캐글의 이상url데이터를 전처리 및 피처를 생성하여 Tree 기반 Ensemble 모델인 Light GBM을 사용하여 학습하여 웹의 사용자의 요청에 대해 예측을 할 수 있도록,
모듈화 시켰습니다.

<br>

파이썬 웹프레임워크인 Flask를 활용하여 웹을 구현하였으며, 사용자가 웹에서 요청을 보낼 시 예측결과를 웹으로 전송하고, Logstash를 통해 예측정보를 Opensearch에 forwarding하여 Opendashboard를 통해 실시간으로 예측정보를 시각화 할 수 있게 구성하여, 추후 분석에 활용할 수 있고, 또한 실시간으로 웹의 악의적인 유저를 탐지하고자 제안하게되었습니다.

배포는 aws의 ec2환경에서 진행되었습니다.


<br>

### 아키텍처 및 디렉토리 구조

<br>

![Untitled](https://user-images.githubusercontent.com/56438131/223625883-e49bc176-0e52-4987-a9c8-c8f945f1bd9e.png)

> **서버1**

웹에서 사용자에게 입력을 받아야하므로, 파이썬 웹서버 프레임워크 Django와 Flask 중에서 비교적 간단히 구현이 가능한 Flask를 선택했다.

사용자의 입력(url)을 불러오고 그값을 파이썬을 통해 파싱한 후 특징을 추출한 후 예측을 하며 예측값은 사용자 화면에 출력되고, 로그생성을 수행하여 logstash에서 opensearch로 forwarding한다.   

> **서버2**

logstash에서 forwarding한 값을 opensearch로 받아온 후 open-dashboard를 연동하여 실시간으로 로그를 수집할 수 있는 서버이다.
