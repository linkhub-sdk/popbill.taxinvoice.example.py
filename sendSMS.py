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
    print("세금계산서 안내문자 재전송")
    
    MgtKeyType = "SELL" #관리번호 유형 , 세금계산서 국세청 즉시전송는 "SELL"/"TRUSTEE"중에서 입력.
    MgtKey = "111-2222-3333"
    Sender = "070-7510-6766" #발신번호
    Receiver = "111-2222-3333" #수신번호
    Contents = "발신문자 내용" # 최대 90bytes.
    UserID = testValue.testUserID

    result = taxinvoiceService.sendSMS(testValue.testCorpNum,MgtKeyType,MgtKey,Sender,Receiver,Contents,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))