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
삭제 가능한 상태의 세금계산서를 삭제합니다.
- 삭제 가능한 상태: "임시저장", "발행취소", "역발행거부", "역발행취소", "전송실패"
- 세금계산서를 삭제해야만 문서번호(mgtKey)를 재사용할 수 있습니다.
- https://docs.popbill.com/taxinvoice/python/api#Delete
'''

try:
    print("=" * 15 + " 세금계산서 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    result = taxinvoiceService.delete(CorpNum, MgtKeyType, MgtKey)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
