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
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
"임시저장" 상태의 세금계산서를 수정합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/issue#Update
'''

try:
    print("=" * 15 + " 세금계산서 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 수정할 세금계산서 문서번호
    MgtKey = "20220803-002"

    # 세금계산서 정보
    taxinvoice = Taxinvoice(

        # 작성일자, 날짜형식(yyyyMMdd)
        writeDate="20220802",

        # 과금방향, '정과금(공급자)', '역과금(공급받는자)'중 기재
        # 역과금의 경우 역발행세금계산서 발행시에만 사용가능
        chargeDirection="정과금",

        # 발행형태, '정발행','역발행','위수탁' 중 기재
        issueType="정발행",

        # {영수, 청구, 없음} 중 기재
        purposeType="영수",

        # 과세형태, {과세, 영세, 면세} 중 기재
        taxType="과세",

        ######################################################################
        #                             공급자 정보
        ######################################################################

        # 공급자 사업자번호, '-' 없이 10자리 기재.
        invoicerCorpNum=testValue.testCorpNum,

        # 공급자 종사업장 식별번호
        invoicerTaxRegID=None,

        # 공급자 상호
        invoicerCorpName="공급자 상호",

        # 공급자 문서번호, 1~24자리, 영문, 숫자, -, _ 조합으로 사업자별로 중복되지 않도록 구성
        invoicerMgtKey=MgtKey,

        # 공급자 대표자 성명
        invoicerCEOName="공급자 대표자 성명_수정",

        # 공급자 주소
        invoicerAddr="공급자 주소_수정",

        # 공급자 종목
        invoicerBizClass="공급자 종목",

        # 공급자 업태
        invoicerBizType="공급자 업태",

        # 공급자 담당자 성명
        invoicerContactName="공급자 담당자명",

        # 공급자 담당자 메일주소
        invoicerEmail="",

        # 공급자 담당자 연락처
        invoicerTEL="",

        # 공급자 담당자 휴대폰 번호
        invoicerHP='',

        # 발행시 알림문자 전송여부 (정발행에서만 사용가능)
        # - 공급받는자 주)담당자 휴대폰번호(invoiceeHP1)로 전송
        # - 전송시 포인트가 차감되며 전송실패하는 경우 포인트 환불처리
        invoicerSMSSendYN=False,

        ######################################################################
        #                            공급받는자 정보
        ######################################################################

        # 공급받는자 구분 '사업자'/'개인'/'외국인' 중 기재
        invoiceeType='사업자',

        # 공급받는자 종사업장 식별번호, 필요시 숫자 4자리 기재
        invoiceeTaxRegID=None,

        # 공급받는자 사업자번호, '-' 제외 10자리
        invoiceeCorpNum='8888888888',

        # 공급받는자 상호
        invoiceeCorpName="공급받는자 상호",

        # [역발행시 필수] 공급받는자 문서번호
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
        invoiceeEmail1="",

        # 공급받는자 연락처
        invoiceeTEL1="",

        # 공급받는자 담당자 휴대폰번호
        invoiceeHP1="",

        # 공급받는자 담당자 팩스번호
        invoiceeFAX1="",

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

        # 비고
        # {invoiceeType}이 "외국인" 이면 remark1 필수
        # - 외국인 등록번호 또는 여권번호 입력
        remark1='비고1',
        remark2='비고2',
        remark3='비고3',

        # 기재상 '권' 항목, 최대값 32767
        # 미기재시 kwon=None,
        kwon=1,

        # 기재상 '호' 항목, 최대값 32767
        # 미기재시 ho=None,
        ho=2,

        # 사업자등록증 이미지 첨부여부  (true / false 중 택 1)
        # └ true = 첨부 , false = 미첨부(기본값)
        # - 팝빌 사이트 또는 인감 및 첨부문서 등록 팝업 URL (GetSealURL API) 함수를 이용하여 등록
        businessLicenseYN=False,

        # 통장사본 이미지 첨부여부  (true / false 중 택 1)
        # └ true = 첨부 , false = 미첨부(기본값)
        # - 팝빌 사이트 또는 인감 및 첨부문서 등록 팝업 URL (GetSealURL API) 함수를 이용하여 등록
        bankBookYN=False,

        ######################################################################
        #                 수정세금계산서 정보 (수정세금계산서 발행시에만 기재)
        # - 수정세금계산서 관련 정보는 연동매뉴얼 또는 개발가이드 링크 참조
        # - [참고] 수정세금계산서 작성방법 안내 - https://developers.popbill.com/reference/taxinvoice/$1/introduction/modified-taxinvoice
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
            purchaseDT="20220803",  # 거래일자, yyyyMMdd
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
            purchaseDT="20220803",  # 거래일자, yyyyMMdd
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

    # 거래명세서 동시작성여부 (true / false 중 택 1)
    # └ true = 사용 , false = 미사용
    # - 미입력 시 기본값 false 처리
    writeSpecification = False

    result = taxinvoiceService.update(CorpNum, MgtKeyType, MgtKey, taxinvoice, writeSpecification)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
