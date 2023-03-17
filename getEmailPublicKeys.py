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
전자세금계산서 유통사업자의 메일 목록을 확인합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/etc#GetEmailPublicKeys
"""

try:
    print("=" * 15 + " 유통사업자 메일 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    aspList = taxinvoiceService.getEmailPublicKeys(CorpNum)

    for asp in aspList:
        print("유통사업자 승인번호[%s]" % asp.confirmNum)
        print("유통사업자 이메일[%s]" % asp.email + "\n")

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
