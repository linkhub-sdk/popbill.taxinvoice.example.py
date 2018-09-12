# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import TaxinvoiceService, PopbillException

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest

'''
팝빌사이트에서 작성된 세금계산서에 파트너 문서관리번호를 할당합니다.
'''

try:
    print("=" * 15 + " 세금계산서 문서관리번호 할당 " + "=" * 15)

    # 팝빌회원 아이디
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 세금계산서 아이템키, 문서 목록조회(Search) API의 반환항목중 ItemKey 참조
    ItemKey = '018081611502800001'

    # 할당할 문서관리번호, 숫자, 영문 '-', '_' 조합으로 1~24자리까지
    # 사업자번호별 중복없는 고유번호 할당
    MgtKey = "20180912-001"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.assignMgtKey(CorpNum, MgtKeyType, ItemKey, MgtKey, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))