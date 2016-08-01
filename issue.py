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
    print("세금계산서 발행")

    MgtKeyType = "SELL" #관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "111-2222-3333"
    Memo = "처리시 메모" #문서이력등에 남는 처리시 메모. 필수 아님.
    EmailSubject = None #발행시 전달되는 메일의 제목 지정. 필수 아님.
    ForceIssue = False #지연발행 세금계산서의 강제발행 여부, False의 경우 지연발행건은 발행되지 않고 예외발생. True로 변경하여 강제발행 가능
    UserID = testValue.testUserID

    result = taxinvoiceService.issue(testValue.testCorpNum,MgtKeyType,MgtKey,Memo,EmailSubject,ForceIssue,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
