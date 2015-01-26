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
    print("대량사업자 유통 이메일 주소 확인")
    aspList = taxinvoiceService.getEmailPublicKeys(testValue.testCorpNum)
    for asp in aspList:
        print("인증번호[%s] : %s" % (asp.confirmNum,asp.email))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))