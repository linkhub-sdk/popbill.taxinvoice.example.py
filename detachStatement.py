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
    print( "=" * 15 + " 전자명세서 첨부해제 " + "=" * 15)

    MgtKeyType = "SELL"        # 세금계산서 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "20160728-03"     # 문서 관리번호
    ItemCode = "121"           # 전자명세서 종류코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    StmtMgtKey = "fbrdavxpsn"  # 전자명세서 문서관리번호

    result = taxinvoiceService.detachStatement(testValue.testCorpNum, MgtKeyType, MgtKey, ItemCode, StmtMgtKey, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
