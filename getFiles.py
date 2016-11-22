# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import TaxinvoiceService, PopbillException

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

'''
세금계산서에 첨부된 파일의 목록을 확인합니다.
- 응답항목 중 파일아이디(AttachedFile) 항목은 파일삭제(DeleteFile API)
  호출시 이용할 수 있습니다.
'''

try:
    print("=" * 15 + " 세금계산서 첨부파일 목록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서 관리번호
    MgtKey = "20161116-01"

    fileList = taxinvoiceService.getFiles(CorpNum, MgtKeyType, MgtKey)

    i = 1
    for f in fileList:
        print("%d:" % i)
        print("serialNum : %s" % f.serialNum)
        print("attachedFile : %s" % f.attachedFile)
        print("displayName : %s" % f.displayName)
        print("regDT : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
