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

from popbill import Taxinvoice, TaxinvoiceDetail, Contact, TaxinvoiceService, PopbillException

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
1건의 세금계산서를 임시저장 합니다.
- 세금계산서 임시저장(Register API) 호출후에는 발행(Issue API)을 호출해야만 국세청으로 전송됩니다.
- 임시저장과 발행을 한번의 호출로 처리하는 즉시발행(RegistIssue API) 프로세스 연동을 권장합니다.
- 세금계산서 항목별 정보는 "[전자세금계산서 API 연동매뉴얼] > 4.1. (세금)계산서 구성"을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 임시저장 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 세금계산서 문서번호, 1~24자리, 영문, 숫자, -, _ 조합으로 사업자별로 중복되지 않도록 구성
    MgtKey = "20190228-002"

    # 거래명세서 동시작성여부
    writeSpecification = False

    # 세금계산서 정보
    taxinvoice = Taxinvoice(

        # 작성일자, 날짜형식(yyyyMMdd)
        writeDate="20190228",

        # 과금방향, '정과금(공급자)', '역과금(공급받는자)'중 기재
        # 역과금의 경우 역발행세금계산서 발행시에만 사용가능
        chargeDirection="정과금",

        # 발행형태, '정발행','역발행','위수탁' 중 기재
        issueType="정발행",

        # '영수'/'청구' 중 기재
        purposeType="영수",

        # 발행시점
        issueTiming="직접발행",

        # 과세형태, '과세'/'영세'/'면세' 중 기재
        taxType="과세",

        ######################################################################
        #                             공급자 정보
        ######################################################################

        # 공급자 사업자번호 , '-' 없이 10자리 기재.
        invoicerCorpNum=testValue.testCorpNum,

        # 공급자 종사업장 식별번호
        invoicerTaxRegID=None,

        # 공급자 상호
        invoicerCorpName="공급자 상호",

        # 공급자 문서번호, 1~24자리, 영문, 숫자, -, _ 조합으로 사업자별로 중복되지 않도록 구성
        invoicerMgtKey=MgtKey,

        # 공급자 대표자 성명
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
        invoicerTEL="070-4304-2991",

        # 공급자 담당자 휴대폰 번호
        invoicerHP='010-1111-2222',

        # 발행시 알림문자 전송여부 (정발행에서만 사용가능)
        # - 공급받는자 주)담당자 휴대폰번호(invoiceeHP1)로 전송
        # - 전송시 포인트가 차감되며 전송실패하는 경우 포인트 환불처리
        invoicerSMSSendYN=False,

        ######################################################################
        #                            공급받는자 정보
        ######################################################################

        # 공급받는자 구분 '사업자'/'개인'/'외국인' 중 기재
        invoiceeType='사업자',

        # 공급받는자 사업자번호, '-' 제외 10자리
        invoiceeCorpNum='8888888888',

        # 공급받는자 상호
        invoiceeCorpName="공급받는자 상호",

        # 공급받는자 문서번호
        invoiceeMgtKey=None,

        # 공급받는자 대표자 성명
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
        # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
        # 실제 거래처의 메일주소가 기재되지 않도록 주의
        invoiceeEmail1="test@test.com",

        # 공급받는자 연락처
        invoiceeTEL1="070-111-222",

        # 공급받는자 담당자 휴대폰번호
        invoiceeHP1="010-2222-1111",

        # 공급받는자 담당자 팩스번호
        invoiceeFAX1="070-4304-2991",

        # 역발행 요청시 알림문자 전송여부 (역발행에서만 사용가능)
        # - 공급자 담당자 휴대폰번호(invoicerHP)로 전송
        # - 전송시 포인트가 차감되며 전송실패하는 경우 포인트 환불처리
        invoiceeSMSSendYN=False,

        ######################################################################
        #                          세금계산서 기재정보
        ######################################################################

        # 공급가액 합계
        supplyCostTotal="100000",

        # 세액 합계
        taxTotal="10000",

        # 합계금액, 공급가액 합계 + 세액 합계
        totalAmount="110000",

        # 기재상 '일련번호' 항목
        serialNum='123',

        # 기재상 '현금' 항목
        cash=None,

        # 기재상 '수표' 항목
        chkBill=None,

        # 기재상 '어음' 항목
        note=None,

        # 기재상 '외상미수금' 항목
        credit='',

        # 기재 상 '비고' 항목
        remark1='비고1',
        remark2='비고2',
        remark3='비고3',

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
        # - [참고] 수정세금계산서 작성방법 안내 - https://docs.popbill.com/taxinvoice/modify?lang=python
        ######################################################################

        # 수정세금계산서 정보
        # 수정사유코드
        modifyCode=None,

        # 원본세금계산서 국세청승인번호 기재
        orgNTSConfirmNum=None
    )

    ######################################################################
    #                           상세항목(품목) 정보
    ######################################################################

    # 상세항목 0~99개 까지 작성가능.
    # 일련번호 (serialNum) 는 1부터 99까지 순차기재.
    taxinvoice.detailList = []

    taxinvoice.detailList.append(
        TaxinvoiceDetail(
            serialNum=1,  # 일련번호, 1부터 순차기재
            purchaseDT="20190116",  # 거래일자, yyyyMMdd
            itemName="품목1",  # 품목
            spec="규격",  # 규격
            qty=1,  # 수량
            unitCost="50000",  # 단가
            supplyCost="50000",  # 공급가액
            tax="5000",  # 세액
            remark="품목비고"  # 비고
        )
    )

    taxinvoice.detailList.append(
        TaxinvoiceDetail(
            serialNum=2,  # 일련번호, 1부터 순차기재
            purchaseDT="20190116",  # 거래일자, yyyyMMdd
            itemName="품목2",  # 품목
            spec="규격",  # 규격
            qty=1,  # 수량
            unitCost="50000",  # 단가
            supplyCost="50000",  # 공급가액
            tax="5000",  # 세액
            remark="품목비고"  # 비고
        )
    )

    ######################################################################
    #                           추가담당자 정보
    # - 세금계산서 발행안내 메일을 수신받을 공급받는자 담당자가 다수인 경우
    #   담당자 정보를 추가하여 발행안내메일을 다수에게 전송할 수 있습니다.
    ######################################################################

    # 최대 5개까지 기재 가능
    taxinvoice.addContactList = []

    taxinvoice.addContactList.append(
        Contact(
            serialNum=1,  # 일련번호, 1부터 순차기재
            contactName="추가담당자 성명",  # 담당자명
            email="test1@test.com"  # 메일주소
        )
    )

    taxinvoice.addContactList.append(
        Contact(
            serialNum=2,  # 일련번호, 1부터 순차기재
            contactName="추가담당자 성명",  # 담당자명
            email="test1@test.com"  # 메일주소
        )
    )

    result = taxinvoiceService.register(CorpNum, taxinvoice, writeSpecification, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
