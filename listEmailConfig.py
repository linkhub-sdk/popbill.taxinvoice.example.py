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
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
세금계산서 관련 메일 항목에 대한 발송설정을 확인합니다.
- https://docs.popbill.com/taxinvoice/python/api#ListEmailConfig
'''

try:
    print("=" * 15 + " 세금계산서 메일전송여부 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    EmailConfig = taxinvoiceService.listEmailConfig(CorpNum)

    for info in EmailConfig:
        if info.emailType == "TAX_ISSUE":
            print("[정발행] %s(공급받는자에게 전자세금계산서 발행 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_ISSUE_INVOICER":
            print("[정발행] %s(공급자에게 전자세금계산서 발행 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_CHECK":
            print("[정발행] %s(공급자에게 전자세금계산서 수신확인 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_CANCEL_ISSUE":
            print("[정발행] %s(공급받는자에게 전자세금계산서 발행취소 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_REQUEST":
            print("[역발행] %s(공급자에게 세금계산서를 발행요청 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_CANCEL_REQUEST":
            print("[역발행] %s(공급받는자에게 세금계산서 취소 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_REFUSE":
            print("[역발행] %s(공급받는자에게 세금계산서 거부 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_TRUST_ISSUE":
            print("[위수탁발행] %s(공급받는자에게 전자세금계산서 발행 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_TRUST_ISSUE_TRUSTEE":
            print("[위수탁발행] %s(수탁자에게 전자세금계산서 발행 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_TRUST_ISSUE_INVOICER":
            print("[위수탁발행] %s(공급자에게 전자세금계산서 발행 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_TRUST_CANCEL_ISSUE":
            print("[위수탁발행] %s(공급받는자에게 전자세금계산서 발행취소 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_TRUST_CANCEL_ISSUE_INVOICER":
            print("[위수탁발행] %s(공급자에게 전자세금계산서 발행취소 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_CLOSEDOWN":
            print("[처리결과] %s(거래처의 휴폐업 여부 확인 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "TAX_NTSFAIL_INVOICER":
            print("[처리결과] %s(전자세금계산서 국세청 전송실패 안내 메일 전송 여부) : %s" % (info.emailType, info.sendYN))
        if info.emailType == "ETC_CERT_EXPIRATION":
            print("[정기발송] %s(팝빌에서 이용중인 공인인증서의 갱신 메일 전송 여부) : %s" % (info.emailType, info.sendYN))


except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
