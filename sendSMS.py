# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import TaxinvoiceService, PopbillException

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

'''
알림문자를 전송합니다. (단문/SMS- 한글 최대 45자)
- 알림문자 전송시 포인트가 차감됩니다. (전송실패시 환불처리)
- 전송내역 확인은 [팝빌 로그인] > [문자 팩스] > [문자] > [전송내역] 메뉴에서 전송결과를 확인할 수 있습니다.
'''

try:
    print("=" * 15 + " 알림문자 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20190108-001"

    # 발신번호
    Sender = "070-8390-1234"

    # 수신번호
    Receiver = "010-8349-0706"

    # 메시지 내용, 최대 90byte 초과시 초과된 내용은 삭제되어 전송
    Contents = "발신문자 내용"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.sendSMS(CorpNum, MgtKeyType, MgtKey, Sender, Receiver,
                                       Contents, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
