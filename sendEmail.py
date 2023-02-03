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
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
발행 안내메일을 재전송합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/etc#SendEmail
'''

try:
    print("=" * 15 + " 발행안내메일 재전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    # 수신자 메일주소
    # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
    # 실제 거래처의 메일주소가 기재되지 않도록 주의
    ReceiverMail = ""

    result = taxinvoiceService.sendEmail(CorpNum, MgtKeyType, MgtKey, ReceiverMail)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code , PE.message))
