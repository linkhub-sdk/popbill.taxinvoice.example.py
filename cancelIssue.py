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
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
[발행완료] 상태의 세금계산서를 [발행취소] 처리합니다.
- [발행취소]는 국세청 전송전에만 가능합니다.
- 발행취소된 세금계산서는 국세청에 전송되지 않습니다.
- 발행취소 세금계산서에 기재된 문서번호를 재사용 하기 위해서는 삭제(Delete API)를 호출하여 [삭제] 처리 하셔야 합니다.
'''

try:
    print("=" * 15 + " 세금계산서 발행 취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20190108-001"

    # 메모
    Memo = "발행취소 메모"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.cancelIssue(CorpNum, MgtKeyType, MgtKey, Memo, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
