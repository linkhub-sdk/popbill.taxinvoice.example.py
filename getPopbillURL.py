# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import TaxinvoiceService,PopbillException

taxinvoiceService =  TaxinvoiceService(testValue.LinkID,testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

try:
    print("팝빌 URL 확인")

    # TOGO : LOGIN-팝빌 로그인 URL, CHRG-팝빌 포인트 충전 URL, CERT-공인인증서 등록, SEAL-인감 및 첨부문서 등록
    TOGO = "SEAL"

    url = taxinvoiceService.getPopbillURL(testValue.testCorpNum,testValue.testUserID,TOGO)

    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
