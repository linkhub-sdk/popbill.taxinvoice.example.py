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
[발행완료] 상태의 세금계산서를 [발행취소] 처리합니다.
- 세금계산서 발행취소는 국세청 전송전에만 가능합니다.
- 발행취소된 세금계산서는 국세청에 전송되지 않습니다.
- 발행취소 세금계산서에 기재된 문서관리번호를 재사용 하기 위해서는
  삭제(Delete API)를 호출하여 [삭제] 처리 하셔야 합니다.
'''

try:
    print("=" * 15 + " 세금계산서 발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20161122-05"

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

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
