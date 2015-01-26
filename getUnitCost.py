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
    print("세금계산서 발행 단가 확인")
    unitCost = taxinvoiceService.getUnitCost(testValue.testCorpNum)
    print("단가: %f" % unitCost)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))