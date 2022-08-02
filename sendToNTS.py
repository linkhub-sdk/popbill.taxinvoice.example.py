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
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
"발행완료" 상태의 전자세금계산서를 국세청에 즉시 전송하며, 함수 호출 후 최대 30분 이내에 전송 처리가 완료됩니다.
- 국세청 즉시전송을 호출하지 않은 세금계산서는 발행일 기준 다음 영업일 오후 3시에 팝빌 시스템에서 일괄적으로 국세청으로 전송합니다.
- https://docs.popbill.com/taxinvoice/python/api#SendToNTS
'''

try:
    print("=" * 15 + " 세금계산서 국세청 즉시전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    result = taxinvoiceService.sendToNTS(CorpNum, MgtKeyType, MgtKey)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code , PE.message))
