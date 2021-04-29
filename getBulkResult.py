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
연동회원의 잔여포인트를 확인합니다.
- 과금방식이 파트너과금인 경우 파트너 잔여포인트(GetPartnerBalance API)
  를 통해 확인하시기 바랍니다.
- https://docs.popbill.com/taxinvoice/python/api#GetBalance
'''

try:
    print("=" * 15 + " 세금계산서 초대량 접수결과 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    #제출아이디
    #최대 36자리 영문, 숫자, '-' 조합으로 구성
    submitID = 'BulkSubmit-PythonShell01'

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    bulkTaxinvoiceResult = taxinvoiceService.getBulkResult(CorpNum, submitID, UserID)

    print("code (요청에 대한 응답 상태코드) : %s " % bulkTaxinvoiceResult.code)
    print("message (요청에 대한 응답 메시지) : %s " % bulkTaxinvoiceResult.message)
    print("submitID (제출아이디) : %s " % bulkTaxinvoiceResult.submitID)
    print("submitCount (세금계산서 접수 건수) : %s " % bulkTaxinvoiceResult.submitCount)
    print("successCount (세금계산서 발행 성공 건수) : %s " % bulkTaxinvoiceResult.successCount)
    print("failCount (세금계산서 발행 실패 건수) : %s " % bulkTaxinvoiceResult.failCount)
    print("txState (접수상태코드) : %s " % bulkTaxinvoiceResult.txState)
    print("txResultCode (접수 결과코드) : %s " % bulkTaxinvoiceResult.txResultCode)
    print("txStartDT (발행처리 시작일시) : %s " % bulkTaxinvoiceResult.txStartDT)
    print("txEndDT (발행처리 완료일시) : %s " % bulkTaxinvoiceResult.txEndDT)
    print("receiptDT (접수일시) : %s " % bulkTaxinvoiceResult.receiptDT)
    print("txEndDT (접수아이디) : %s " % bulkTaxinvoiceResult.txEndDT)

    print("=" * 15 + " issueResult (발행결과) " + "=" * 15)
    for bulkTaxinvoiceIssueResult in bulkTaxinvoiceResult.issueResult:
        print("invoicerMgtKey (공급자 문서번호) : %s " % bulkTaxinvoiceIssueResult.invoicerMgtKey)
        print("invoicerMgtKey (수탁자 문서번호) : %s " % bulkTaxinvoiceIssueResult.invoicerMgtKey)
        print("code (응답코드) : %s " % bulkTaxinvoiceIssueResult.code)
        print("ntsconfirmNum (국세청승인번호) : %s " % bulkTaxinvoiceIssueResult.ntsconfirmNum)
        print("issueDT (발행일시) : %s " % bulkTaxinvoiceIssueResult.issueDT)
        print("*" * 50)
        
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
