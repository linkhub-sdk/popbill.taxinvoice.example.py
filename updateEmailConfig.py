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
전자세금계산서 관련 메일전송 항목에 대한 전송여부를 수정합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/etc#UpdateEmailConfig

메일전송유형
[정발행]
TAX_ISSUE_INVOICER : 공급자에게 전자세금계산서 발행 사실을 안내하는 메일
TAX_CHECK : 공급자에게 전자세금계산서 수신확인 사실을 안내하는 메일
TAX_CANCEL_ISSUE : 공급받는자에게 전자세금계산서 발행취소 사실을 안내하는 메일

[역발행]
TAX_REQUEST : 공급자에게 전자세금계산서를 발행을 요청하는 메일
TAX_CANCEL_REQUEST : 공급받는자에게 전자세금계산서 취소 사실을 안내하는 메일
TAX_REFUSE : 공급받는자에게 전자세금계산서 거부 사실을 안내하는 메일
TAX_REVERSE_ISSUE : 공급받는자에게 전자세금계산서 발행 사실을 안내하는 메일

[위수탁발행]
TAX_TRUST_ISSUE : 공급받는자에게 전자세금계산서 발행 사실을 안내하는 메일
TAX_TRUST_ISSUE_TRUSTEE : 수탁자에게 전자세금계산서 발행 사실을 안내하는 메일
TAX_TRUST_ISSUE_INVOICER : 공급자에게 전자세금계산서 발행 사실을 안내하는 메일
TAX_TRUST_CANCEL_ISSUE : 공공급받는자에게 전자세금계산서 발행취소 사실을 안내하는 메일
TAX_TRUST_CANCEL_ISSUE_INVOICER : 공급자에게 전자세금계산서 발행취소 사실을 안내하는 메일

[처리결과]
TAX_CLOSEDOWN : 거래처의 사업자등록상태(휴폐업)를 확인하여 안내하는 메일
TAX_NTSFAIL_INVOICER : 전자세금계산서 국세청 전송실패를 안내하는 메일

[정기발송]
ETC_CERT_EXPIRATION : 팝빌에 등록된 인증서의 만료예정을 안내하는 메일
"""

try:
    print("=" * 15 + " 세금계산서 메일전송여부 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 메일 전송 유형
    EmailType = "TAX_ISSUE_INVOICER"

    # 전송 여부 (True = 전송, False = 미전송)
    SendYN = True

    result = taxinvoiceService.updateEmailConfig(CorpNum, EmailType, SendYN)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
