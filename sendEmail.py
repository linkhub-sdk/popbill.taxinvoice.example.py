# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import TaxinvoiceService, PopbillException

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP

'''
세금계산서 발행 안내메일을 재전송합니다.
- https://docs.popbill.com/taxinvoice/python/api#SendEmail
'''

try:
    print("=" * 15 + " 발행안내메일 재전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20190108-001"

    # 수신자 메일주소
    # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
    # 실제 거래처의 메일주소가 기재되지 않도록 주의
    ReceiverMail = "test@test.com"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.sendEmail(CorpNum, MgtKeyType, MgtKey, ReceiverMail, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code , PE.message))
