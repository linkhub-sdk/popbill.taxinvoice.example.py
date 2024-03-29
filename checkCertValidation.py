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
팝빌에 등록된 공인인증서의 유효성을 확인합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/cert#CheckCertValidation
"""

try:
    print("=" * 15 + " 공인인증서 유효성 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = "1234567890"

    result = taxinvoiceService.checkCertValidation(CorpNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
