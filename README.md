홍익대학교 서울캠/세종캠 학식정보 크롤링 
===
***
- Language : Python3

- 홍익대학교 서울캠퍼스, 세종캠퍼스 오늘의 학식정보를 JSON으로 반환해주는 코드입니다

- 반환되는 JSON파일의 이름은 다음과 같이 반환됩니다.

    - HongikUnivSeoulCampusCafeteria + 오늘날짜

    - HongikUnivSejongCampusCafeteria + 오늘날짜

- 추후 만약 학식업체가 변경된다는 등의 사유로 구조가 변경되는경우에는 그때그때 대응할 예정입니다.

- 홍익대학교 서울캠/세종캠 학생분들중 같이 코드를 발전시킬분(Contributers가 되실분)은 언제든지 환영합니다
***
- API 

    - 해당 Repository의 API는 Flask 프레임워크를 이용해 간단하게만 만든 API입니다(Apache, mod_wsgi 등 적용안함)
    
    - Default Port : 5000 (Flask)
    
    - HTTP Method : GET

    - 응답형식 : JSON 
    
    - 설명

        - /seoul : 서울캠퍼스 정보의 JSON을 응답합니다

        - /sejong : 세종캠퍼스 정보의 JSON을 응답합니다
    
