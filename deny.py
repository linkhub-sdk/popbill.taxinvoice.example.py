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
발행예정 세금계산서를 [거부]처리 합니다.
- [거부]된 세금계산서를 삭제(Delete API)하면 등록된 문서관리번호를
  재사용할 수 있습니다.
'''

try:
    print("=" * 15 + " 발행예정 세금계산서 거부 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20161117-01"

    # 메모
    Memo = "발행예정 거부 메모"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.deny(CorpNum, MgtKeyType, MgtKey, Memo, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
