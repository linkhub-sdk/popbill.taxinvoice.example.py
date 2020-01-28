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
[임시저장] 또는 [발행대기] 상태의 세금계산서를 [공급자]가 [발행]합니다.
- https://docs.popbill.com/taxinvoice/python/api#TIIssue
'''

try:
    print("=" * 15 + " 세금계산서 발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20190228-002"

    # 메모
    Memo = "발행 메모"

    # 발행 안내메일 제목, 미기재시 기본양식으로 전송
    EmailSubject = None

    # 지연발행 강제여부, 기본값 - False
    # 발행마감일이 지난 세금계산서를 발행하는 경우, 가산세가 부과될 수 있습니다.
    # 지연발행 세금계산서를 신고해야 하는 경우 forceIssue 값을 True로 선언하여
    # 발행(Issue API)을 호출할 수 있습니다.
    ForceIssue = False

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.issue(CorpNum, MgtKeyType, MgtKey, Memo,
                                     EmailSubject, ForceIssue, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
    print("국세청승인번호 : %s" % (result.ntsConfirmNum))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
