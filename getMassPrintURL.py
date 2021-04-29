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
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
다수건의 전자세금계산서 인쇄팝업 URL을 반환합니다. (최대 100건)
- 반환된 URL은 보안정책에 따라 30초의 유효시간을 갖습니다.
- https://docs.popbill.com/taxinvoice/python/api#GetMassPrintURL
'''

try:
    print("=" * 15 + " 세금계산서 인쇄 팝업 URL (대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 인쇄할 문서번호 배열, 최대 100건
    MgtKeyList = []
    MgtKeyList.append("20190116-01")
    MgtKeyList.append("20190116-02")
    MgtKeyList.append("20190116-03")

    url = taxinvoiceService.getMassPrintURL(CorpNum, MgtKeyType, MgtKeyList)
    print("URL: %s" % url)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
