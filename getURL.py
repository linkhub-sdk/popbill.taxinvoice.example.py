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
    print("세금계산서 관련 URL 확인")

    togo = "SBOX" # SBOX : 매출보관함, PBOX : 매입보관함 , TBOX : 임시문서함 , WRITE : 문서작성

    url = taxinvoiceService.getURL(testValue.testCorpNum,testValue.testUserID,togo)
    print("URL: %s" % url)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))