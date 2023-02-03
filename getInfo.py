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
세금계산서 1건의 상태 및 요약정보를 확인합니다.
- 리턴값 'TaxinvoiceInfo'의 변수 'stateCode'를 통해 세금계산서의 상태코드를 확인합니다.
- 세금계산서 상태코드 [https://developers.popbill.com/reference/taxinvoice/$2/response-code#state-code]
- https://developers.popbill.com/reference/taxinvoice/python/api/info#GetInfo
'''

try:
    print("=" * 15 + " 세금계산서 상태/요약 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    taxinvoiceInfo = taxinvoiceService.getInfo(CorpNum, MgtKeyType, MgtKey)

    print("세금계산서 정보>")
    print("itemKey (팝빌번호) : %s " % taxinvoiceInfo.itemKey)
    print("taxType (과세형태) : %s " % taxinvoiceInfo.taxType)
    print("writeDate (작성일자) : %s " % taxinvoiceInfo.writeDate)
    print("regDT (임시저장 일자) : %s " % taxinvoiceInfo.regDT)
    print("issueType (발행형태) : %s " % taxinvoiceInfo.issueType)
    print("supplyCostTotal (공급가액 합계) : %s " % taxinvoiceInfo.supplyCostTotal)
    print("taxTotal (세액 합계) : %s " % taxinvoiceInfo.taxTotal)
    print("purposeType (영수/청구) : %s " % taxinvoiceInfo.purposeType)
    print("issueDT (발행일시) : %s " % taxinvoiceInfo.issueDT)
    print("lateIssueYN (지연발행 여부) : %s " % taxinvoiceInfo.lateIssueYN)
    print("openYN (개봉 여부) : %s " % taxinvoiceInfo.openYN)
    print("openDT (개봉 일시) : %s " % taxinvoiceInfo.openDT)
    print("stateMemo (상태메모) : %s " % taxinvoiceInfo.stateMemo)
    print("stateCode (상태코드) : %s " % taxinvoiceInfo.stateCode)
    print("ntsconfirmNum (국세청승인번호) : %s " % taxinvoiceInfo.ntsconfirmNum)
    print("ntsresult (국세청 전송결과) : %s " % taxinvoiceInfo.ntsresult)
    print("ntssendDT (국세청 전송일시) : %s " % taxinvoiceInfo.ntssendDT)
    print("ntsresultDT (국세청 결과 수신일시) : %s " % taxinvoiceInfo.ntsresultDT)
    print("ntssendErrCode (전송실패 사유코드) : %s " % taxinvoiceInfo.ntssendErrCode)
    print("modifyCode (수정 사유코드) : %s " % taxinvoiceInfo.modifyCode)
    print("interOPYN (연동문서 여부) : %s " % taxinvoiceInfo.interOPYN)

    print("\n공급자, 공급받는자, 수탁자 정보>")
    print("invoicerCorpName (공급자 상호) : %s " % taxinvoiceInfo.invoicerCorpName)
    print("invoicerCorpNum (공급자 사업자번호) : %s " % taxinvoiceInfo.invoicerCorpNum)
    print("invoicerMgtKey (공급자 문서번호) : %s " % taxinvoiceInfo.invoicerMgtKey)
    print("invoicerPrintYN (공급자 인쇄여부) : %s " % taxinvoiceInfo.invoicerPrintYN)
    print("invoiceeCorpName (공급받는자 상호) : %s " % taxinvoiceInfo.invoiceeCorpName)
    print("invoiceeCorpNum (공급받는자 사업자번호) : %s " % taxinvoiceInfo.invoiceeCorpNum)
    print("invoiceePrintYN (공급받는자 인쇄여부) : %s " % taxinvoiceInfo.invoiceePrintYN)
    print("closeDownState (공급받는자 휴폐업상태) : %s " % taxinvoiceInfo.closeDownState)
    print("closeDownStateDate (공급받는자 휴폐업일자) : %s " % taxinvoiceInfo.closeDownStateDate)
    print("trusteeCorpName (수탁자 상호) : %s " % taxinvoiceInfo.trusteeCorpName)
    print("trusteeCorpNum (수탁자 사업자번호) : %s " % taxinvoiceInfo.trusteeCorpNum)
    print("trusteeMgtKey (수탁자 문서번호) : %s " % taxinvoiceInfo.trusteeMgtKey)
    print("trusteePrintYN (수탁자 인쇄여부) : %s " % taxinvoiceInfo.trusteePrintYN + "\n")
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
