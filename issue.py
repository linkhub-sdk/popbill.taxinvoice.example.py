# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import PopbillException, TaxinvoiceService

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
"임시저장" 또는 "(역)발행대기" 상태의 세금계산서를 발행(전자서명)하며, "발행완료" 상태로 처리합니다.
- 세금계산서 국세청 전송정책 [https://developers.popbill.com/guide/taxinvoice/python/introduction/policy-of-send-to-nts]
- "발행완료" 된 전자세금계산서는 국세청 전송 이전에 발행취소(CancelIssue API) 함수로 국세청 신고 대상에서 제외할 수 있습니다.
- 세금계산서 발행을 위해서 공급자의 인증서가 팝빌 인증서버에 사전등록 되어야 합니다.
    └ 위수탁발행의 경우, 수탁자의 인증서 등록이 필요합니다.
- 세금계산서 발행 시 공급받는자에게 발행 메일이 발송됩니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/issue#Issue
"""

try:
    print("=" * 15 + " 세금계산서 발행 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-002"

    # 메모
    Memo = "발행 메모"

    # 발행 안내메일 제목, 미기재시 기본양식으로 전송
    EmailSubject = None

    # 지연발행 강제여부, 기본값 - False
    # 발행마감일이 지난 세금계산서를 발행하는 경우, 가산세가 부과될 수 있습니다.
    # 지연발행 세금계산서를 신고해야 하는 경우 forceIssue 값을 True로 선언하여
    # 발행(Issue API)을 호출할 수 있습니다.
    ForceIssue = False

    result = taxinvoiceService.issue(
        CorpNum, MgtKeyType, MgtKey, Memo, EmailSubject, ForceIssue
    )

    print("처리결과 : [%d] %s" % (result.code, result.message))
    print("국세청승인번호 : %s" % (result.ntsConfirmNum))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
