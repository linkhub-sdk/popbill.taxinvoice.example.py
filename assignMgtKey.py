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
팝빌 사이트를 통해 발행하여 문서번호가 부여되지 않은 세금계산서에 문서번호를 할당합니다.
- https://docs.popbill.com/taxinvoice/python/api#AssignMgtKey
'''

try:
    print("=" * 15 + " 세금계산서 문서번호 할당 " + "=" * 15)

    # 팝빌회원 아이디
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 세금계산서 아이템키, 문서 목록조회(Search) API의 반환항목중 ItemKey 참조
    ItemKey = '022072217590500001'

    # 할당할 문서번호, 숫자, 영문 '-', '_' 조합으로 1~24자리까지
    # 사업자번호별 중복없는 고유번호 할당
    MgtKey = "20220803-001"

    result = taxinvoiceService.assignMgtKey(CorpNum, MgtKeyType, ItemKey, MgtKey)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
