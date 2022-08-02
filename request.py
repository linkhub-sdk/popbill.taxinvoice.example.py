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
공급받는자가 저장된 역발행 세금계산서를 공급자에게 송부하여 발행 요청합니다.
- 역발행 세금계산서 프로세스를 구현하기 위해서는 공급자/공급받는자가 모두 팝빌에 회원이여야 합니다.
- 역발행 요청후 공급자가 [발행] 처리시 포인트가 차감되며 역발행 세금계산서 항목중 과금방향(ChargeDirection) 에 기재한 값에 따라
  정과금(공급자과금) 또는 역과금(공급받는자과금) 처리됩니다.
- https://docs.popbill.com/taxinvoice/python/api#Request
'''

try:
    print("=" * 15 + " 세금계산서 역발행요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    # 메모
    Memo = "역발행 요청 메모"

    result = taxinvoiceService.request(CorpNum, MgtKeyType, MgtKey, Memo)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code , PE.message))
