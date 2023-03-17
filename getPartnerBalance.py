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
파트너의 잔여포인트를 확인합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/point#GetPartnerBalance
"""

try:
    print("=" * 15 + " 파트너 잔여포인트 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    balance = taxinvoiceService.getPartnerBalance(CorpNum)

    print("파트너 잔여포인트: %f" % balance)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
