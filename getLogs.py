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
    print("세금계산서 처리이력 목록")
    
    MgtKeyType = "SELL" #관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "111-2222-3333"
   
    LogList = taxinvoiceService.getLogs(testValue.testCorpNum,MgtKeyType,MgtKey)

    ''' TaxinvoiceLog 구성: 
            docLogType : 이력유형
            log : 문서이력 설명
            procType : 처리유형
            procCorpName : 처리회사명
            procMemo : 처리시 메모
            regDT : 처리일시
    '''
    i = 1
    for f in LogList:
        print("%d:" % i)
        print("    docLogType : %s" % f.docLogType)
        print("    log : %s" % f.log)
        print("    procType : %s" % f.procType)
        print("    procCorpName : %s" % f.procCorpName)
        print("    procMemo : %s" % f.procMemo)
        print("    regDT : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))