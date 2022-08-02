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
팝빌 인증서버에 등록된 인증서의 만료일을 확인합니다.
- https://docs.popbill.com/taxinvoice/python/api#GetCertificateExpireDate
'''

try:
    print("=" * 15 + " 공인인증서 만료일시 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = "1234567890"

    expiredate = taxinvoiceService.getCertificateExpireDate(CorpNum)

    print("공인인증서 만료일시: %s" % expiredate)
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
