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
1건의 전자세금계산서 보기 팝업 URL을 반환합니다. (메뉴/버튼 제외)
- 보안정책으로 인해 반환된 URL의 유효시간은 30초입니다.
- https://docs.popbill.com/taxinvoice/python/api#GetViewURL
'''

try:
    print("=" * 15 + " 세금계산서 보기 팝업 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20210429-001"

    url = taxinvoiceService.getViewURL(CorpNum, MgtKeyType, MgtKey)
    print("URL: %s" % url)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code , PE.message))
