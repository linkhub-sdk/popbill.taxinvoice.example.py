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
    print("등록 공인인증서 등록여부 및 만료일자 확인")
    expiredate = taxinvoiceService.getCertificateExpireDate(testValue.testCorpNum)
    print("만료일시: %s" % expiredate)
except PopbillException as PE:
    #인증서 미등록시 PopbillException [code : -10002009] "등록된 공인인증서가 없습니다." 발생.
    if PE.code == -10002009:
        print("인증서 미등록")
    else:
        print("Exception Occur : [%d] %s" % (PE.code , PE.message))