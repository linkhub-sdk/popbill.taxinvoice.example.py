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
1건의 세금계산서 상세항목을 확인합니다.
- 응답항목에 대한 자세한 사항은 "[전자세금계산서 API 연동매뉴얼]  > 4.1 (세금)계산서 구성" 을
  참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서 관리번호
    MgtKey = "20190116-001"

    taxinvoice = taxinvoiceService.getDetailInfo(CorpNum, MgtKeyType, MgtKey)

    print("writeDate (작성일자) : %s " % taxinvoice.writeDate)
    print("chargeDirection (과금방향) : %s " % taxinvoice.chargeDirection)
    print("issueType (발행형태) : %s " % taxinvoice.issueType)
    print("issueTiming (발행시점) : %s " % taxinvoice.issueTiming)
    print("taxType (과세형태) : %s " % taxinvoice.taxType)
    print("supplyCostTotal (공급가액 합계) : %s " % taxinvoice.supplyCostTotal)
    print("taxTotal (세액 합계) : %s " % taxinvoice.taxTotal)
    print("totalAmount (합계금액) : %s " % taxinvoice.totalAmount)
    print("ntsconfirmNum (국세청승인번호) : %s " % taxinvoice.ntsconfirmNum)
    print("invoicerCorpNum (공급자 사업자번호) : %s " % taxinvoice.invoicerCorpNum)
    print("invoicerMgtKey (공급자 문서관리번호) : %s " % taxinvoice.invoicerMgtKey)
    print("invoicerCorpName (공급자 상호) : %s " % taxinvoice.invoicerCorpName)
    print("invoicerCEOName (공급자 대표자명) : %s " % taxinvoice.invoicerCEOName)
    print("invoicerAddr (공급자 주소) : %s " % taxinvoice.invoicerAddr)
    print("invoicerContactName (공급자 담당자명) : %s " % taxinvoice.invoicerContactName)
    print("invoicerTEL (공급자 담당자 연락처) : %s " % taxinvoice.invoicerTEL)
    print("invoicerHP (공급자 담당자 휴대폰) : %s " % taxinvoice.invoicerHP)
    print("invoicerEmail (공급자 담당자 메일) : %s " % taxinvoice.invoicerEmail)
    print("invoicerSMSSendYN (발행안내문자 전송여부) : %s " % taxinvoice.invoicerSMSSendYN)
    print("invoiceeCorpNum (공급받는자 사업자번호) : %s " % taxinvoice.invoiceeCorpNum)
    print("invoiceeType (공급받는자 구분) : %s " % taxinvoice.invoiceeType)
    print("invoiceeMgtKey (공급받는자 문서관리번호) : %s " % taxinvoice.invoiceeMgtKey)
    print("invoiceeCorpName (공급받는자 상호) : %s " % taxinvoice.invoiceeCorpName)
    print("invoiceeCEOName (공급받는자 대표자명) : %s " % taxinvoice.invoiceeCEOName)
    print("invoiceeAddr (공급받는자 주소) : %s " % taxinvoice.invoiceeAddr)
    print("invoiceeContactName1 (공급받는자 담당자명) : %s " % taxinvoice.invoiceeContactName1)
    print("invoiceeTEL1 (공급받는자 담당자 연락처) : %s " % taxinvoice.invoiceeTEL1)
    print("invoiceeHP1 (공급받는자 담당자 휴대폰) : %s " % taxinvoice.invoiceeHP1)
    print("invoiceeEmail1 (공급받는자 담당자 메일) : %s " % taxinvoice.invoiceeEmail1)
    print("invoiceeSMSSendYN (역발행안내문자 전송여부) : %s " % taxinvoice.invoiceeSMSSendYN)
    print("closeDownState (공급받는자 휴폐업상태) : %s " % taxinvoice.closeDownState)
    print("closeDownStateDate (공급받는자 휴폐업일자) : %s " % taxinvoice.closeDownStateDate)
    print("purposeType (영수/청구) : %s " % taxinvoice.purposeType)
    print("serialNum (일련번호) : %s " % taxinvoice.serialNum)
    print("remark1 (비고1) : %s " % taxinvoice.remark1)
    print("remark2 (비고2) : %s " % taxinvoice.remark2)
    print("remark3 (비고3) : %s " % taxinvoice.remark3)
    print("kwon (권) : %s " % taxinvoice.kwon)
    print("ho(호) : %s " % taxinvoice.ho)
    print("businessLicenseYN (사업자등록증 이미지 첨부여부) : %s " % taxinvoice.businessLicenseYN)
    print("bankBookYN (통장사본이미지 첨부여부) : %s " % taxinvoice.bankBookYN) + "\n"

    print("=" * 15 + "상세항목(품목) 정보" + "=" * 15)
    if taxinvoice.detailList is not None:
        for detailList in taxinvoice.detailList:
            print("serialNum (일련번호) : %s " % detailList.serialNum)
            print("purchaseDT (거래일자) : %s " % detailList.purchaseDT)
            print("itemName (품명) : %s " % detailList.itemName)
            print("spec (규격) : %s " % detailList.spec)
            print("qty (수량) : %s " % detailList.qty)
            print("unitCost (단가) : %s " % detailList.unitCost)
            print("supplyCost (공급가액) : %s " % detailList.supplyCost)
            print("tax (세액) : %s " % detailList.tax)
            print("remark (비고) : %s " % detailList.remark + "\n")

    print("=" * 15 + "추가담당자 정보" + "=" * 15)
    if taxinvoice.addContactList is not None:
        for addContactList in taxinvoice.addContactList:
            print("serialNum (일련번호) : %s " % addContactList.serialNum)
            print("contactName (담당자 성명) : %s " % addContactList.contactName)
            print("email (이메일주소) : %s " % addContactList.email + "\n")

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
