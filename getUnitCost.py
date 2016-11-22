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
전자세금계산서 발행단가를 확인합니다.
'''

try:
    print("=" * 15 + " 세금계산서 발행단가 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    unitCost = taxinvoiceService.getUnitCost(CorpNum)

    print("발행단가 : %d" % unitCost)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
