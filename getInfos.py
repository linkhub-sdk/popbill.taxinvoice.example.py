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
다수건의 세금계산서 상태 및 요약 정보를 확인합니다. (1회 호출 시 최대 1,000건 확인 가능)
- 리턴값 'TaxinvoiceInfo'의 변수 'stateCode'를 통해 세금계산서의 상태코드를 확인합니다.
- 세금계산서 상태코드 [https://developers.popbill.com/reference/taxinvoice/python/response-code#state-code]
- https://developers.popbill.com/reference/taxinvoice/python/api/info#GetInfos
"""

try:
    print("=" * 15 + " 세금계산서 상태/요약 정보 확인 (대량) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호 배열, 최대 1000건
    MgtKeyList = []
    MgtKeyList.append("20220803-001")
    MgtKeyList.append("20220803-002")
    MgtKeyList.append("20220803-003")

    InfoList = taxinvoiceService.getInfos(CorpNum, MgtKeyType, MgtKeyList)

    for info in InfoList:
        print("\n======세금계산서 정보======>")
        print("itemKey (팝빌번호) : %s " % info.itemKey)
        print("taxType (과세형태) : %s " % info.taxType)
        print("writeDate (작성일자) : %s " % info.writeDate)
        print("regDT (임시저장 일자) : %s " % info.regDT)
        print("issueType (발행형태) : %s " % info.issueType)
        print("supplyCostTotal (공급가액 합계) : %s " % info.supplyCostTotal)
        print("taxTotal (세액 합계) : %s " % info.taxTotal)
        print("purposeType (영수/청구) : %s " % info.purposeType)
        print("issueDT (발행일시) : %s " % info.issueDT)
        print("lateIssueYN (지연발행 여부) : %s " % info.lateIssueYN)
        print("openYN (개봉 여부) : %s " % info.openYN)
        print("openDT (개봉 일시) : %s " % info.openDT)
        print("stateMemo (상태메모) : %s " % info.stateMemo)
        print("stateCode (상태코드) : %s " % info.stateCode)
        print("ntsconfirmNum (국세청승인번호) : %s " % info.ntsconfirmNum)
        print("ntsresult (국세청 전송결과) : %s " % info.ntsresult)
        print("ntssendDT (국세청 전송일시) : %s " % info.ntssendDT)
        print("ntsresultDT (국세청 결과 수신일시) : %s " % info.ntsresultDT)
        print("ntssendErrCode (전송실패 사유코드) : %s " % info.ntssendErrCode)
        print("modifyCode (수정 사유코드) : %s " % info.modifyCode)
        print("interOPYN (연동문서 여부) : %s " % info.interOPYN)

        print("\n공급자, 공급받는자, 수탁자 정보>")
        print("invoicerCorpName (공급자 상호) : %s " % info.invoicerCorpName)
        print("invoicerCorpNum (공급자 사업자번호) : %s " % info.invoicerCorpNum)
        print("invoicerMgtKey (공급자 문서번호) : %s " % info.invoicerMgtKey)
        print("invoicerPrintYN (공급자 인쇄여부) : %s " % info.invoicerPrintYN)
        print("invoiceeCorpName (공급받는자 상호) : %s " % info.invoiceeCorpName)
        print("invoiceeCorpNum (공급받는자 사업자번호) : %s " % info.invoiceeCorpNum)
        print("invoiceePrintYN (공급받는자 인쇄여부) : %s " % info.invoiceePrintYN)
        print("closeDownState (공급받는자 휴폐업상태) : %s " % info.closeDownState)
        print("closeDownStateDate (공급받는자 휴폐업일자) : %s " % info.closeDownStateDate)
        print("trusteeCorpName (수탁자 상호) : %s " % info.trusteeCorpName)
        print("trusteeCorpNum (수탁자 사업자번호) : %s " % info.trusteeCorpNum)
        print("trusteeMgtKey (수탁자 문서번호) : %s " % info.trusteeMgtKey)
        print("trusteePrintYN (수탁자 인쇄여부) : %s " % info.trusteePrintYN + "\n")
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
