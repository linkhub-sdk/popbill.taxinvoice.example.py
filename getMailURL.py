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
전자세금계산서 안내메일의 상세보기 링크 URL을 반환합니다.
- 함수 호출로 반환 받은 URL에는 유효시간이 없습니다.
- https://docs.popbill.com/taxinvoice/python/api#GetMailURL
'''

try:
    print("=" * 15 + " 세금계산서 메일링크 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    url = taxinvoiceService.getMailURL(CorpNum, MgtKeyType, MgtKey, UserID)
    print("URL: %s" % url)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code , PE.message))
