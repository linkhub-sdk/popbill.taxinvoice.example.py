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

from popbill import TaxinvoiceService, PopbillException, Taxinvoice, TaxinvoiceDetail

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
세금계산서 대량 발행을 접수합니다. (최대 100건)
- https://docs.popbill.com/taxinvoice/python/api#BulkSubmit
'''

try:
    print("=" * 15 + " 세금계산서 초대량 발행 접수 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    #제출아이디
    #최대 36자리 영문, 숫자, '-' 조합으로 구성
    submitID = 'BulkSubmit-PythonShell01'

    # 지연발행 강제여부
    # 발행마감일이 지난 세금계산서를 발행하는 경우, 가산세가 부과될 수 있습니다.
    # 가산세가 부과되더라도 발행을 해야하는 경우에는 forceIssue의 값을 True로 선언
    forceIssue = False

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    #세금계산서 객체정보 리스트
    taxinvoicelist = []
    for i in range(0,20):
        taxinvoicelist.append(
            Taxinvoice(
                # [필수] 작성일자, 날짜형식(yyyyMMdd) ex)20190116
                writeDate="20210429",

                # [필수] 과금방향, [정과금(공급자), 역과금(공급받는자)]중 기재
                # 역과금의 경우 역발행세금계산서 발행시에만 사용가능
                chargeDirection="정과금",

                # [필수] 발행형태, [정발행, 역발행, 위수탁] 중 기재
                issueType="정발행",

                # [필수] 영수/청구, [영수, 청구] 중 기재
                purposeType="영수",

                # [필수] 과세형태, [과세, 영세, 면세] 중 기재
                taxType="과세",

                ######################################################################
                #                             공급자 정보
                ######################################################################

                # [필수] 공급자 사업자번호 , '-' 없이 10자리 기재.
                invoicerCorpNum=testValue.testCorpNum,

                # 공급자 종사업장 식별번호, 필요시 숫자 4자리 기재
                invoicerTaxRegID=None,

                # [필수] 공급자 상호
                invoicerCorpName="공급자 상호",

                # [필수] 공급자 문서번호, 1~24자리, (영문, 숫자, '-', '_') 조합으로
                # 사업자별로 중복되지 않도록 구성
                invoicerMgtKey=submitID + '-' + str(i),

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

                # 발행시 알림문자 전송여부 (정발행에서만 사용가능)
                # - 공급받는자 주)담당자 휴대폰번호(invoiceeHP1)로 전송
                # - 전송시 포인트가 차감되며 전송실패하는 경우 포인트 환불처리
                invoicerSMSSendYN=False,

                ######################################################################
                #                            공급받는자 정보
                ######################################################################

                # [필수] 공급받는자 구분, [사업자, 개인, 외국인] 중 기재
                invoiceeType="사업자",

                # [필수] 공급받는자 사업자번호, '-' 제외 10자리
                invoiceeCorpNum="8888888888",

                # 공급자 종사업장 식별번호, 필요시 숫자 4자리 기재
                invoiceeTaxRegID=None,

                # [필수] 공급받는자 상호
                invoiceeCorpName="BulkTEST 상호",

                # [역발행시 필수] 공급받는자 문서번호, 1~24자리 (숫자, 영문, '-', '_') 조합으로 사업자별로 중복되지 않도록 구성
                invoiceeMgtKey=None,

                # [필수] 공급받는자 대표자 성명
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
                # 팝빌 개발환경에서 테스트하는 경우에도 안내 메일이 전송되므로,
                # 실제 거래처의 메일주소가 기재되지 않도록 주의
                invoiceeEmail1="test@test.com",

                # 공급받는자 연락처
                invoiceeTEL1="070-111-222",

                # 공급받는자 담당자 휴대폰번호
                invoiceeHP1="010-111-222",

                # 공급받는자 담당자 팩스번호
                invoiceeFAX1="070-111-222",

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
                serialNum="123",

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
                #                           상세항목(품목) 정보
                ######################################################################

                # 상세항목 0~99개 까지 작성가능.
                # 일련번호 (serialNum) 는 1부터 99까지 순차기재.
                detailList=[
                    TaxinvoiceDetail(
                        serialNum=1,
                        purchaseDT='20210428',
                        itemName="품목1",
                        spec='규격',
                        qty=1,
                        unitCost='100000',
                        supplyCost='100000',
                        tax='10000',
                        remark='품목비고'
                    )
                ]
            )
        )

    bulkResponse = taxinvoiceService.bulkSubmit(CorpNum, submitID, taxinvoicelist, forceIssue, UserID)

    print("처리결과 : [%d] %s" % (bulkResponse.code, bulkResponse.message))
    print("접수번호 : %s" % (bulkResponse.receiptID))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
