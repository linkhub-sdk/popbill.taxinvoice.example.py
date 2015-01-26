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
    print("세금계산서 다량 인쇄 URL")
    MgtKeyType = "SELL" #관리번호 유형 , 세금계산서 국세청 즉시전송는 "SELL"/"TRUSTEE"중에서 입력.
    MgtKeyList = ["111-2222-3333","1234","1234567890"]
    UserID = testValue.testUserID

    url = taxinvoiceService.getMassPrintURL(testValue.testCorpNum,MgtKeyType,MgtKeyList,UserID)
    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))