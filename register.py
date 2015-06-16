# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Taxinvoice,TaxinvoiceDetail,Contact,TaxinvoiceService,PopbillException

taxinvoiceService =  TaxinvoiceService(testValue.LinkID,testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
  
try:
    print("세금계산서 1건 임시저장")
    
    taxinvoice = Taxinvoice(writeDate = "20150616", #작성일자 yyyyMMdd
                            chargeDirection = "정과금", #과금방향 '정과금' , '역과금' 역발행시에만 '역과금' 기능 사용가능
                            issueType = "정발행", #발행영태 '정발행','역발행','위수탁'
                            purposeType = "영수", # '영수'/'청구'
                            issueTiming = "직접발행", # '직접발행' / '승인시자동발행'
                            taxType = "과세", # '과세'/'영세'/'면세'
                            invoicerCorpNum = testValue.testCorpNum, # 공급자 사업자번호 , '-' 없이 10자리 기재.
                            invoicerTaxRegID = None, # 공급자 종사업자 식별번호, 공급자가 사업자단위과세제도를 운영하여, 이를 세금계산서에 기재하고자 할 경우 국세청에서 부여한 식별번호 4자리 입력.
                            invoicerCorpName = "공급자 상호", 
                            invoicerMgtKey = "20150616-22", #파트너 부여 세금계산서 관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성
                            invoicerCEOName = "공급자 대표자 성명",
                            invoicerAddr = "공급자 주소",
                            invoicerBizClass = "공급자 업종",
                            invoicerBizType = "공급자 업태",
                            invoicerContactName = "공급자 담당자명",
                            invoicerEmail = "test@test.com", #공급자 이메일주소
                            invoicerTEL = "070-7510-6766", # 공급자 담당자연락처
                            invoicerHP = '010-1111-2222', # 공급자 휴대전화 번호
                            invoicerSMSSendYN = False, # 공급자가 공급받는자에게 발행시 발행안내문자를 보내고자 할경우 설정. 수신자 번호는 invoiceeHP1에 기재.

                            invoiceeType = '사업자', #공급받는자 유형 '사업자'/'개인'/'외국인'
                            invoiceeCorpNum = '8888888888', #공급받는자 사업자번호 '-' 없이 10자리 또는 주민번호 13자리. '외국인'의 경우 9999999999999 를 개지.
                            invoiceeCorpName = "공급받는자 상호_#$@#$!<>&_Python",
                            invoiceeMgtKey = None, # 파트너 부여 세금계산서 관리번호, 역발행시에는 공급받는자에 기재.
                            invoiceeCEOName = "공급받는자 상호",
                            invoiceeAddr = "공급받는자 주소",
                            invoiceeBizClass = "공급받는자 업종",
                            invoiceeBizType = "공급받는자 업태",
                            invoiceeContactName1 = "공급받는자 담당자",
                            invoiceeEmail1 = "test@test.com", # 공급받는자 이메일주소
                            invoiceeHP1 = "010-2222-1111", # 공급받는자 휴대전화 번호
                            invoiceeFAX1 = "070-7510-6767", #공급받는자 팩스번호
                            invoiceeSMSSendYN = False, # 공급받는자가 공급자에게 역발행요청시 안내문자를 보내고자 할경우 설정. 수신자 번호는 invoicerHP에 기재.

                            supplyCostTotal = "100000", # 공급가액 총액
                            taxTotal = "10000", # 세액 총액
                            totalAmount = "110000", # 합계금액, 공급가액 총액 + 세액 총액
                            
                            modifyCode = None, # 수정사유코드 수정세금계산서 작성시에 1~6까지 사유코드를 기재. 수정사유코드기재시에만 수정세금계산서로 처리함.
                            originalTaxinvoiceKey = None, # 수정세금계산서 작성시에 원본 세금계산서의 ItemKey를 기재, ItemKey 는 getInfo()를 통해 확인.
                            serialNum = '123', # 기재상 일련번호
                            cash = '', # 기재상 현금
                            chkBill = None, #기재상 수표
                            note = None, #기재상 어음
                            credit = '', #기재상 외상미수금
                            remark1 = '비고1',
                            remark2 = '비고2',
                            remark3 = '비고3',
                            kwon = 1, # 기재상 권 항목
                            ho = 2, # 기재상 호 항목

                            businessLicenseYN  = False, # 사업자등록증 이미지 첨부여부, 사업자등록증 이미지는 팝빌에 로그인하여 등록가능
                            bankBookYN = False # 통장사본 이미지 첨부여부, 통장사본 이미지는 팝빌에 로그인하여 등록가능
                            )
    # 세금계산서 하단 상세항목 0~99개까지 기재 가능,  serialNum은 1부터 순서대로 기재. 각항목의 세액의 합계는 계산서의 세액합계액과 같아야함.
    taxinvoice.detailList = [
                                TaxinvoiceDetail(serialNum = 1,  #일련번호
                                                 purchaseDT = '20150121', #거래일자, yyyyMMdd
                                                 itemName="품목1", # 품목
                                                 spec = '규격', # 규격
                                                 qty = 1, #수량
                                                 unitCost = '100000', # 단가
                                                 supplyCost = '100000', # 공급가액
                                                 tax = '10000', # 세액
                                                 remark = '품목비고' #비고
                                                 ), 
                                TaxinvoiceDetail(serialNum = 2,
                                                 itemName = "품목2")
                            ]
    # 세금계산서 공급받는자 추가 담당자 설정. invoiceeEmail1 이외에 추가메일을 수신하고자 하는 담당자를 기재, 최대 5까지 기재 가능.
    taxinvoice.addContactList = [
                                    Contact(serialNum = 1, 
                                            contactName='추가담당자 성명',
                                            email='test1@test.com'),
                                    Contact(serialNum = 2,
                                            contactName='추가담당자2',
                                            email='test2@test.com')
                                ]
    
    writeSpecification = False
    UserID = testValue.testUserID

    result = taxinvoiceService.register(testValue.testCorpNum,taxinvoice,writeSpecification,UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))