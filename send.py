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
    print("세금계산서 승인요청")

    MgtKeyType = "SELL" #관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "20150616-22"
    Memo = "처리시 메모" #문서이력등에 남는 처리시 메모. 필수 아님.
    UserID = testValue.testUserID
    EmailSubject = "" # 전송메일 제목, 미기재시 기본제목으로 전송

    result = taxinvoiceService.send(testValue.testCorpNum,MgtKeyType,MgtKey,Memo,EmailSubject,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
