# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import PopbillException, TaxinvoiceService

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
세금계산서 1건의 상세정보를 XML로 반환합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/info#GetXML
"""

try:
    print("=" * 15 + " 상세정보 확인 - XML " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    taxinvoiceXML = taxinvoiceService.getXML(CorpNum, MgtKeyType, MgtKey)

    print("세금계산서 정보>")
    print("code (응답코드) : %s " % taxinvoiceXML.code)
    print("message (응답메시지) : %s " % taxinvoiceXML.message)
    print("retObject (전자세금계산서 XML문서) : %s " % taxinvoiceXML.retObject)
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
