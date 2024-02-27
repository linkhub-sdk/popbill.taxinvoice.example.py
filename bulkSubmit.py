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
from popbill import PopbillException, Taxinvoice, TaxinvoiceDetail, TaxinvoiceService

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
최대 100건의 세금계산서 발행을 한번의 요청으로 접수합니다.
- 세금계산서 발행을 위해서 공급자의 인증서가 팝빌 인증서버에 사전등록 되어야 합니다.
    └ 위수탁발행의 경우, 수탁자의 인증서 등록이 필요합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/issue#BulkSubmit
"""

try:
    print("=" * 15 + " 세금계산서 초대량 발행 접수 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 제출아이디
    # 최대 36자리 영문, 숫자, '-' 조합으로 구성
    submitID = "PYTHON-BULK"

    # 지연발행 강제여부  (true / false 중 택 1)
    # └ true = 가능 , false = 불가능
    # - 발행마감일이 지난 세금계산서를 발행하는 경우, 가산세가 부과될 수 있습니다.
    # - 가산세가 부과되더라도 발행을 해야하는 경우에는 forceIssue의 값을
    #   true로 선언하여 발행(Issue API)를 호출하시면 됩니다.
    forceIssue = False

    # 세금계산서 객체정보 리스트
    taxinvoicelist = []
    for i in range(0, 20):
        taxinvoicelist.append(
            Taxinvoice(
                # 작성일자, 날짜형식(yyyyMMdd) ex)20220803
                writeDate="20220803",
                # 정과금 기재
                chargeDirection="정과금",
                # 발행형태, {정발행, 위수탁} 중 기재
                issueType="정발행",
                # {영수, 청구, 없음} 중 기재
                purposeType="영수",
                # 과세형태, {과세, 영세, 면세} 중 기재
                taxType="과세",
                ######################################################################
                #                             공급자 정보
                ######################################################################
                # 공급자 사업자번호 , '-' 없이 10자리 기재.
                invoicerCorpNum=testValue.testCorpNum,
                # 공급자 종사업장 식별번호, 필요시 숫자 4자리 기재
                invoicerTaxRegID=None,
                # 공급자 상호
                invoicerCorpName="공급자 상호",
                # 공급자 문서번호, 1~24자리, (영문, 숫자, '-', '_') 조합으로
                # 사업자별로 중복되지 않도록 구성
                invoicerMgtKey=submitID + "-" + str(i),
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
                invoicerEmail="",
                # 공급자 담당자 연락처
                invoicerTEL="",
                # 공급자 담당자 휴대폰 번호
                invoicerHP="",
                # 발행 안내 문자 전송여부 (true / false 중 택 1)
                # └ true = 전송 , false = 미전송
                # └ 공급받는자 (주)담당자 휴대폰번호 {invoiceeHP1} 값으로 문자 전송
                # - 전송 시 포인트 차감되며, 전송실패시 환불처리
                invoicerSMSSendYN=False,
                ######################################################################
                #                            공급받는자 정보
                ######################################################################
                # 공급받는자 구분, [사업자, 개인, 외국인] 중 기재
                invoiceeType="사업자",
                # 공급받는자 사업자번호
                # - {invoiceeType}이 "사업자" 인 경우, 사업자번호 (하이픈 ('-') 제외 10자리)
                # - {invoiceeType}이 "개인" 인 경우, 주민등록번호 (하이픈 ('-') 제외 13자리)
                # - {invoiceeType}이 "외국인" 인 경우, "9999999999999" (하이픈 ('-') 제외 13자리)
                invoiceeCorpNum="8888888888",
                # 공급자 종사업장 식별번호, 필요시 숫자 4자리 기재
                invoiceeTaxRegID=None,
                # 공급받는자 상호
                invoiceeCorpName="BulkTEST 상호",
                # 공급받는자 대표자 성명
                invoiceeCEOName="BulkTEST 대표자 성명",
                # 공급받는자 주소
                invoiceeAddr="BulkTEST 주소",
                # 공급받는자 종목
                invoiceeBizClass="BulkTEST 종목",
                # 공급받는자 업태
                invoiceeBizType="BulkTEST 업태",
                # 공급받는자 담당자 성명
                invoiceeContactName1="BulkTEST 담당자",
                # 공급받는자 담당자 메일주소
                # 팝빌 테스트 환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
                # 실제 거래처의 메일주소가 기재되지 않도록 주의
                invoiceeEmail1="",
                # 공급받는자 연락처
                invoiceeTEL1="",
                # 공급받는자 담당자 휴대폰번호
                invoiceeHP1="",
                # 공급받는자 담당자 팩스번호
                invoiceeFAX1="",
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
                serialNum="123",
                # 기재상 '현금' 항목
                cash=None,
                # 기재상 '수표' 항목
                chkBill=None,
                # 기재상 '어음' 항목
                note=None,
                # 기재상 '외상미수금' 항목
                credit="",
                # 기재상 '권' 항목, 최대값 32767
                # 미기재시 kwon=None,
                kwon=1,
                # 기재상 '호' 항목, 최대값 32767
                # 미기재시 ho=None,
                ho=2,
                # 비고
                # {invoiceeType}이 "외국인" 이면 remark1 필수
                # - 외국인 등록번호 또는 여권번호 입력
                remark1="비고1",
                remark2="비고2",
                remark3="비고3",
                # 사업자등록증 이미지 첨부여부  (true / false 중 택 1)
                # └ true = 첨부 , false = 미첨부(기본값)
                # - 팝빌 사이트 또는 인감 및 첨부문서 등록 팝업 URL (GetSealURL API) 함수를 이용하여 등록
                businessLicenseYN=False,
                # 통장사본 이미지 첨부여부  (true / false 중 택 1)
                # └ true = 첨부 , false = 미첨부(기본값)
                # - 팝빌 사이트 또는 인감 및 첨부문서 등록 팝업 URL (GetSealURL API) 함수를 이용하여 등록
                bankBookYN=False,
                ######################################################################
                #                           상세항목(품목) 정보
                ######################################################################
                # 상세항목 0~99개 까지 작성가능.
                # 일련번호 (serialNum) 는 1부터 99까지 순차기재.
                detailList=[
                    TaxinvoiceDetail(
                        serialNum=1,
                        purchaseDT="20220803",
                        itemName="품목1",
                        spec="규격",
                        qty=1,
                        unitCost="100000",
                        supplyCost="100000",
                        tax="10000",
                        remark="품목비고",
                    )
                ],
            )
        )

    bulkResponse = taxinvoiceService.bulkSubmit(
        CorpNum, submitID, taxinvoicelist, forceIssue
    )

    print("처리결과 : [%d] %s" % (bulkResponse.code, bulkResponse.message))
    print("접수번호 : %s" % (bulkResponse.receiptID))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
