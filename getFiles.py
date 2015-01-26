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
    print("세금계산서 첨부파일 목록")
    
    MgtKeyType = "SELL" #관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "111-2222-3333"
   
    fileList = taxinvoiceService.getFiles(testValue.testCorpNum,MgtKeyType,MgtKey)

    ''' attachedFile 구성: 
            attachedFile : #파일 삭제시에 활용되는 파일 ID
            regDT :    #등록일시 yyyyMMddHHmmss
            displayName : 표시명
            serialNum : 일련번호
    '''
    i = 1
    for f in fileList:
        print("%d:" % i)
        print("    serialNum : %s" % f.serialNum)
        print("    attachedFile : %s" % f.attachedFile)
        print("    displayName : %s" % f.displayName)
        print("    regDT : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))