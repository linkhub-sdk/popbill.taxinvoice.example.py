# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import TaxinvoiceService, PopbillException

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

'''
세금계산서에 첨부된 전자명세서 1건을 첨부해제합니다.
'''

try:
    print("=" * 15 + " 전자명세서 첨부해제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서 관리번호
    MgtKey = "20190108-002"

    # 첨부해제할 전자명세서 종류코드, 121-거래명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    ItemCode = "121"

    # 첨부해제할 전자명세서 문서관리번호
    StmtMgtKey = "20190116-001"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.detachStatement(CorpNum, MgtKeyType, MgtKey,
                                               ItemCode, StmtMgtKey, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
