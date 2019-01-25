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

'''
대용량 연계사업자 메일주소 목록을 반환합니다.
'''

try:
    print("=" * 15 + " 대용량사업자 유통 메일 주소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    aspList = taxinvoiceService.getEmailPublicKeys(CorpNum)

    for asp in aspList:
        print("인증번호[%s] : %s" % (asp.confirmNum, asp.email))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
