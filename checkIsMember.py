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
파트너의 연동회원으로 가입된 사업자 번호인지 확안합니다.
- https://docs.popbill.com/taxinvoice/python/api#CheckIsMember
'''

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 가입여부 확인할 사업자번호
    CorpNum = "1234567890"

    result = taxinvoiceService.checkIsMember(CorpNum)

    print("가입여부 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
