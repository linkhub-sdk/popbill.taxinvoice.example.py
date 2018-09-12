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
전자세금계산서 관련 메일 전송 여부전송 항목에 대한 전송여부를 목록으로 반환합니다
'''

try:
    print("=" * 15 + " 세금계산서 메일 전송 여부 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    EmailConfig = taxinvoiceService.listEmailConfig(CorpNum, UserID)

    for info in EmailConfig:
        if info.emailType == "TAX_ISSUE":
            print info.emailType, "(공급받는자에게 전자세금계산서 발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_ISSUE_INVOICER":
            print info.emailType, "(공급자에게 전자세금계산서 발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_CHECK":
            print info.emailType, "(공급자에게 전자세금계산서 수신확인 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_CANCEL_ISSUE":
            print info.emailType, "(공급받는자에게 전자세금계산서 발행취소 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_SEND":
            print info.emailType, "(공급받는자에게 [발행예정] 세금계산서 발송 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_ACCEPT":
            print info.emailType, "(공급자에게 [발행예정] 세금계산서 승인 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_ACCEPT_ISSUE":
            print info.emailType, "(공급자에게 [발행예정] 세금계산서 자동발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_DENY":
            print info.emailType, "(공급자에게 [발행예정] 세금계산서 거부 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_CANCEL_SEND":
            print info.emailType, "(공급받는자에게 [발행예정] 세금계산서 취소 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_REQUEST":
            print info.emailType, "(공급자에게 세금계산서를 발행요청 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_CANCEL_REQUEST":
            print info.emailType, "(공급받는자에게 세금계산서 취소 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_REFUSE":
            print info.emailType, "(공급받는자에게 세금계산서 거부 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_ISSUE":
            print info.emailType, "(공급받는자에게 전자세금계산서 발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_ISSUE_TRUSTEE":
            print info.emailType, "(수탁자에게 전자세금계산서 발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_ISSUE_INVOICER":
            print info.emailType, "(공급자에게 전자세금계산서 발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_CANCEL_ISSUE":
            print info.emailType, "(공급받는자에게 전자세금계산서 발행취소 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_CANCEL_ISSUE_INVOICER":
            print info.emailType, "(공급자에게 전자세금계산서 발행취소 메) :", info.sendYN
        if info.emailType == "TAX_TRUST_SEND":
            print info.emailType, "(공급받는자에게 [발행예정] 세금계산서 발송 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_ACCEPT":
            print info.emailType, "(수탁자에게 [발행예정] 세금계산서 승인 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_ACCEPT_ISSUE":
            print info.emailType, "(수탁자에게 [발행예정] 세금계산서 자동발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_DENY":
            print info.emailType, "(수탁자에게 [발행예정] 세금계산서 거부 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_TRUST_CANCEL_SEND":
            print info.emailType, "(공급받는자에게 [발행예정] 세금계산서 취소 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_CLOSEDOWN":
            print info.emailType, "(거래처의 휴폐업 여부 확인 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_NTSFAIL_INVOICER":
            print info.emailType, "(전자세금계산서 국세청 전송실패 안내 메일 전송 여부) :", info.sendYN
        if info.emailType == "TAX_SEND_INFO":
            print info.emailType, "(전월 귀속분 [매출 발행 대기] 세금계산서 발행 메일 전송 여부) :", info.sendYN
        if info.emailType == "ETC_CERT_EXPIRATION":
            print info.emailType, "(팝빌에서 이용중인 공인인증서의 갱신 메일 전송 여부) :", info.sendYN


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
