# -*- coding: utf-8 -*-

'''
 팝빌 전자세금계산서 API Python SDK Example

 - Python SDK 연동환경 설정방법 안내 : http://blog.linkhub.co.kr/581
 - 업데이트 일자 : 2017-05-24
 - 연동 기술지원 연락처 : 1600-8536 / 070-4304-2991
 - 연동 기술지원 이메일 : code@linkhub.co.kr

 <테스트 연동개발 준비사항>
 1) 21, 24번 라인에 선언된 링크아이디(LinkID)와 비밀키(SecretKey)를
    링크허브 가입시 메일로 발급받은 인증정보를 참조하여 변경합니다.
 2) 팝빌 개발용 사이트(test.popbill.com)에 연동회원으로 가입합니다.
 3) 전자세금계산서 발행을 위해 공인인증서를 등록합니다.
    - 팝빌사이트 로그인 > [전자세금계산서] > [환경설정] > [공인인증서 관리]
    - 공인인증서 등록 팝업 URL (GetPopbillURL API)을 이용하여 등록
'''

# 링크아이디
LinkID = 'TESTER'

# 비밀키
SecretKey = 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I='

# 연동환경 설정값, 개발용(True), 상업용(False)
IsTest = True

# 팝빌회원 사업자번호
testCorpNum = "1234567890"

# 팝빌회원 아아디
testUserID = "testkorea"
