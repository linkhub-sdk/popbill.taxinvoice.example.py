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
연동회원의 국세청 전송 옵션 설정 상태를 확인합니다.
- 세금계산서 국세청 전송 정책 [https://developers.popbill.com/guide/taxinvoice/python/introduction/policy-of-send-to-nts]
- 국세청 전송 옵션 설정은 팝빌 사이트 [전자세금계산서] > [환경설정] > [세금계산서 관리] 메뉴에서 설정할 수 있으며, API로 설정은 불가능 합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/etc#GetSendToNTSConfig
"""

try:
    print("=" * 15 + " 국세청 전송 설정 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    sendToNTSConfig = taxinvoiceService.getSendToNTSConfig(CorpNum)

    print("sendToNTS: %s" % sendToNTSConfig)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
