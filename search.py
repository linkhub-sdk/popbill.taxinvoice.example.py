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
검색조건을 사용하여 세금계산서 목록을 조회합니다. (조회기간 단위 : 최대 6개월)
- https://docs.popbill.com/taxinvoice/python/api#Search
'''

try:
    print("=" * 15 + " 세금계산서 목록 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 세금계산서 유형 SELL-매출, BUY-매입, TRUSTEE-위수탁
    MgtKeyType = "SELL"

    # 조회일자유형, W-작성일자, R-등록일자, I-발행일자
    DType = "W"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20210401"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20210430"

    # 세금계산서 상태코드 배열, 2,3번째 자리에 와일드카드(*) 사용가능
    State = ["3**", "6**"]

    # 문서유형 배열, N-일반 세금계산서, M-수정 세금계산서
    Type = ["N", "M"]

    # 과세형태 배열, T-과세, N-면세, Z-영세
    TaxType = ["T", "N", "Z"]

    # 발행형태 배열, N-정발행, R-역발행, T-위수탁
    IssueType = ["N", "R", "T"]

    # 등록유형 배열, P-팝빌 등록, H-홈택스, 외부ASP
    RegType = ["P", "H"]

    # 공급받는자 사업자 휴폐업상태 배열, N-미확인, 0-미등록, 1-사업중, 2-폐업, 3-휴업
    CloseDownState = ["N", "0", "1", "2", "3"]

    # 지연발행 여부, 공백-전체조회, 0-정상발행, 1-지연발행
    LateOnly = ""

    # 종사업장번호 유무, 공백-전체조회, 0-종사업장번호 없음, 1-종사업장번호 있음
    TaxRegIDYN = ""

    # 종사업장번호 사업자유형, S-공급자, B-공급받는자, T-수탁자
    TaxRegIDType = "S"

    # 종사업장번호, 다수작성시 콤마(",")로 구분하여 구성 ex) "0001,0007"
    TaxRegID = ""

    # 페이지번호, 기본값 '1'
    Page = 1

    # 페이지당 검색개수, 기본값 500, 최대 1000
    PerPage = 5

    # 정렬 방향, D-내림차순, A-오름차순
    Order = "D"

    # 거래처 정보, 거래처 상호 또는 사업자등록번호 기재, 공백처리시 전체조회
    QString = ""

    # 연동문서 조회여부, 공백-전체조회, 0-일반문서 조회, 1-연동문서조회
    InterOPYN = ""

    # 전자세금계산서 문서번호 또는 국세청승인번호 조회
    MgtKey = ""

    response = taxinvoiceService.search(CorpNum, MgtKeyType, DType,
                                        SDate, EDate, State, Type, TaxType, LateOnly, TaxRegIDYN,
                                        TaxRegIDType, TaxRegID, Page, PerPage, Order, UserID,
                                        QString, InterOPYN, IssueType, RegType, CloseDownState, MgtKey)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for info in response.list:
        print("itemKey (팝빌 관리번호) : %s " % info.itemKey)
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
        print("trusteePrintYN (수탁자 인쇄여부) : %s " % info.trusteePrintYN)
        print("*" * 50)
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
