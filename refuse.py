# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Taxinvoice,TaxinvoiceDetail,Contact,TaxinvoiceService,PopbillException

taxinvoiceService =  TaxinvoiceService(testValue.LinkID,testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
  
try:
    print("세금계산서 역)발행요청 거부")
    
    MgtKeyType = "SELL" #관리번호 유형 , 역발행요청 거부는 "BUY"로 고정
    MgtKey = "111-2222-3333"
    Memo = "처리시 메모" #문서이력등에 남는 처리시 메모. 필수 아님.
    UserID = testValue.testUserID

    result = taxinvoiceService.refuse(testValue.testCorpNum,MgtKeyType,MgtKey,Memo,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))