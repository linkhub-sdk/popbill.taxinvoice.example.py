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
역발행 세금계산서를 [취소] 처리합니다.
- [취소]한 세금계산서의 문서관리번호를 재사용하기 위해서는 삭제 (Delete API)
  를 호출해야 합니다.
'''
try:
    print("=" * 15 + "세금계산서 역발행요청 취소" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20161122-06"

    # 메모
    Memo = "처리시 메모"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.cancelRequest(CorpNum, MgtKeyType, MgtKey, Memo, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
