# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import TaxinvoiceService,PopbillException

taxinvoiceService =  TaxinvoiceService(testValue.LinkID,testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 세금계산서 목록 조회 " + "=" * 15)

    # 세금계산서 유형 SELL-매출, BUY-매입, TRUSTEE-위수탁
    MgtKeyType = "SELL"

    # 조회일자유형, W-작성일자, R-등록일자, I-발행일자
    DType = "W"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20160601"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20160831"

    # 세금계산서 상태코드 배열, 2,3번째 자리에 와일드카드(*) 사용가능
    State = ["3**", "6**"]

    # 문서유형 배열, N-일반 세금계산서, M-수정 세금계산서
    Type = ["N", "M"]

    # 과세형태 배열, T-과세, N-면세, Z-영세
    TaxType = ["T", "N", "Z"]

    # 지연발행 여부, 0-정상발행, 1-지연발행
    LateOnly = ""

    # 종사업장번호 유무, 공백-전체조회, 0-종사업장번호 없음, 1-종사업장번호 있음
    TaxRegIDYN = ""

    # 종사업장번호 사업자유형, S-공급자, B-공급받는자, T-수탁자
    TaxRegIDType = "S"

    # 종사업장번호, 다수작성시 콤마(",")로 구분하여 구성 ex) "0001,0007"
    TaxRegID = ""

    # 페이지번호
    Page = 1

    # 페이지당 검색개수
    PerPage = 10

    # 정렬 방향, D-내림차순, A-오름차순
    Order = "D"

    response = taxinvoiceService.search(testValue.testCorpNum, MgtKeyType, DType, SDate, EDate, State, Type,
                                    TaxType, LateOnly, TaxRegIDYN, TaxRegIDType, TaxRegID, Page, PerPage,
                                    Order, testValue.testUserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    i = 1
    for info in response.list :
        print("====== 세금계산서 정보 [%d] ======"% i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print()


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))