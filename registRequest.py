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

from popbill import TaxinvoiceService, PopbillException, Taxinvoice, TaxinvoiceDetail, Contact

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

'''
[공급받는자]가 공급자에게 1건의 역발행 세금계산서를 [즉시 요청]합니다.
  - 세금계산서 항목별 정보는 "[전자세금계산서 API 연동매뉴얼] > 4.1. (세금)계산서구성"을 참조하시기 바랍니다.
  - 역발행 세금계산서 프로세스를 구현하기 위해서는 공급자/공급받는자가 모두 팝빌에 회원이여야 합니다.
  - 역발행 즉시요청후 공급자가 [발행] 처리시 포인트가 차감되며 역발행 세금계산서 항목중 과금방향(ChargeDirection)에 기재한 값에 따라
    정과금(공급자과금) 또는 역과금(공급받는자과금) 처리됩니다.
'''

try:
    print("=" * 15 + " 세금계산서 즉시 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 세금계산서 정보
    taxinvoice = Taxinvoice(

        # [필수] 작성일자, 날짜형식(yyyyMMdd) ex)20180116
        writeDate="20190115",

        # [필수] 과금방향, [정과금(공급자), 역과금(공급받는자)]중 기재
        # 역과금의 경우 역발행세금계산서 발행시에만 사용가능
        chargeDirection="정과금",

        # [필수] 발행영태, [정발행, 역발행, 위수탁] 중 기재
        issueType="역발행",

        # [필수] 영수/청구, [영수, 청구] 중 기재
        purposeType="영수",

        # [필수] 발행시점, [직접발행, 승인시자동발행] '중 기재
        # 발행예정(Send API) 프로세스를 구현하지 않는경우 "직접발행' 기재
        issueTiming="직접발행",

        # [필수] 과세형태, [과세, 영세, 면세] 중 기재
        taxType="과세",

        ######################################################################
        #                             공급자 정보
        ######################################################################

        # [필수] 공급자 사업자번호 , '-' 없이 10자리 기재.
        invoicerCorpNum="8888888888",

        # 공급자 종사업장 식별번호, 필요시 숫자 4자리 기재
        invoicerTaxRegID=None,

        # [필수] 공급자 상호
        invoicerCorpName="공급자 상호",

        # 공급자 문서관리번호, 1~24자리, (영문, 숫자, '-', '_') 조합으로
        # 사업자별로 중복되지 않도록 구성
        invoicerMgtKey="",

        # [필수] 공급자 대표자 성명
        invoicerCEOName="공급자 대표자 성명",

        # 공급자 주소
        invoicerAddr="공급자 주소",

        # 공급자 종목
        invoicerBizClass="공급자 종목",

        # 공급자 업태
        invoicerBizType="공급자 업태",

        # 공급자 담당자 성명
        invoicerContactName="공급자 담당자명",

        # 공급자 담당자 메일주소
        invoicerEmail="test@test.com",

        # 공급자 담당자 연락처
        invoicerTEL="070-111-222",

        # 공급자 담당자 휴대폰 번호
        invoicerHP='010-111-222',

        # 정발행시 공급받는자에게 발행안내문자 전송여부
        invoicerSMSSendYN=False,

        ######################################################################
        #                            공급받는자 정보
        ######################################################################

        # [필수] 공급받는자 구분, [사업자, 개인, 외국인] 중 기재
        invoiceeType="사업자",

        # [필수] 공급받는자 사업자번호, '-' 제외 10자리
        invoiceeCorpNum=CorpNum,

        # 공급자 종사업장 식별번호, 필요시 숫자 4자리 기재
        invoiceeTaxRegID=None,

        # [필수] 공급받는자 상호
        invoiceeCorpName="공급받는자 상호",

        # [역발행시 필수] 공급받는자 문서관리번호, 1~24자리 (숫자, 영문, '-', '_') 조합으로
        # 사업자별로 중복되지 않도록 구성
        invoiceeMgtKey="20190115-1010",

        # [필수] 공급받는자 대표자 성명
        invoiceeCEOName="공급받는자 대표자 성명",

        # 공급받는자 주소
        invoiceeAddr="공급받는자 주소",

        # 공급받는자 종목
        invoiceeBizClass="공급받는자 종목",

        # 공급받는자 업태
        invoiceeBizType="공급받는자 업태",

        # 공급받는자 담당자 성명
        invoiceeContactName1="공급받는자 담당자",

        # 공급받는자 담당자 메일주소
        invoiceeEmail1="test@test.com",

        # 공급받는자 연락처
        invoiceeTEL1="070-111-222",

        # 공급받는자 담당자 휴대폰번호
        invoiceeHP1="010-111-222",

        # 공급받는자 담당자 팩스번호
        invoiceeFAX1="070-111-222",

        # 역발행시 공급자에게 발행안내문자 전송여부
        invoiceeSMSSendYN=False,

        ######################################################################
        #                          세금계산서 기재정보
        ######################################################################

        # [필수] 공급가액 합계
        supplyCostTotal="100000",

        # [필수] 세액 합계
        taxTotal="10000",

        # [필수] 합계금액, 공급가액 합계 + 세액 합계
        totalAmount="110000",

        # 기재상 '일련번호' 항목
        serialNum="",

        # 기재상 '현금' 항목
        cash=None,

        # 기재상 '수표' 항목
        chkBill=None,

        # 기재상 '어음' 항목
        note=None,

        # 기재상 '외상미수금' 항목
        credit="",

        # 기재 상 '비고' 항목
        remark1="비고1",
        remark2="비고2",
        remark3="비고3",

        # 기재상 '권' 항목, 최대값 32767
        # 미기재시 kwon=None,
        kwon=1,

        # 기재상 '호' 항목, 최대값 32767
        # 미기재시 ho=None,
        ho=2,

        # 사업자등록증 이미지 첨부여부
        businessLicenseYN=False,

        # 통장사본 이미지 첨부여부
        bankBookYN=False,

        ######################################################################
        #                 수정세금계산서 정보 (수정세금계산서 발행시에만 기재)
        # - 수정세금계산서 관련 정보는 연동매뉴얼 또는 개발가이드 링크 참조
        # - [참고] 수정세금계산서 작성방법 안내 - http://blog.linkhub.com/650
        ######################################################################

        # 수정세금계산서 정보 수정사유별로 1~6중 선택기재
        # 수정사유코드
        modifyCode=None,

        # 원본 세금계산서 ItemKey, 문서확인 (GetInfo API)의 응답결과(ItemKey 항목) 확인.
        originalTaxinvoiceKey=None
    )

    ######################################################################
    #                           상세항목(품목) 정보
    ######################################################################

    # 상세항목 0~99개 까지 작성가능.
    # 일련번호 (serialNum) 는 1부터 99까지 순차기재.
    taxinvoice.detailList = [
        TaxinvoiceDetail(
            serialNum=1,  # 일련번호, 1부터 순차기재
            purchaseDT="20190108",  # 거래일자, yyyyMMdd
            itemName="품목1",  # 품목
            spec="규격",  # 규격
            qty=1,  # 수량
            unitCost="50000",  # 단가
            supplyCost="50000",  # 공급가액
            tax="5000",  # 세액
            remark="품목비고"  # 비고
        ),
        TaxinvoiceDetail(
            serialNum=2,  # 일련번호, 1부터 순차기재
            purchaseDT="20190108",  # 거래일자, yyyyMMdd
            itemName="품목2",  # 품목
            spec="규격",  # 규격
            qty=1,  # 수량
            unitCost="50000",  # 단가
            supplyCost="50000",  # 공급가액
            tax="5000",  # 세액
            remark="품목비고"  # 비고
        )
    ]

    ######################################################################
    #                           추가담당자 정보
    # - 세금계산서 발행안내 메일을 수신받을 공급받는자 담당자가 다수인 경우
    #   담당자 정보를 추가하여 발행안내메일을 다수에게 전송할 수 있습니다.
    ######################################################################

    # 최대 5개까지 기재 가능
    taxinvoice.addContactList = [
        Contact(
            serialNum=1,  # 일련번호, 1부터 순차기재
            contactName="추가담당자 성명",  # 담당자명
            email="support@linkhub.co.kr"  # 메일주소
        ),
        Contact(
            serialNum=2,  # 일련번호, 1부터 순차기재
            contactName="추가담당자 성명",  # 담당자명
            email="code@linkhub.co.kr"  # 메일주소
        )
    ]

    # 즉시요청 메모
    memo = "즉시요청 메모"

    result = taxinvoiceService.registRequest(CorpNum, taxinvoice, memo, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
