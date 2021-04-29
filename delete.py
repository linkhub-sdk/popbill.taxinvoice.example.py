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
1건의 전자세금계산서를 삭제합니다.
- 세금계산서를 삭제해야만 문서번호(mgtKey)를 재사용할 수 있습니다.
- 삭제가능한 문서 상태 : 임시저장, 발행취소, 역)발행 거부/취소
- https://docs.popbill.com/taxinvoice/python/api#Delete
'''

try:
    print("=" * 15 + " 세금계산서 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20190108-001"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.delete(CorpNum, MgtKeyType, MgtKey, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
