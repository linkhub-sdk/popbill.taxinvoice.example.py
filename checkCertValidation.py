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
팝빌에 등록된 공인인증서의 유효성을 확인합니다.
'''

try:
    print("=" * 15 + " 공인인증서 유효성 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = "1234567890"

    result = taxinvoiceService.checkCertValidation(CorpNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
