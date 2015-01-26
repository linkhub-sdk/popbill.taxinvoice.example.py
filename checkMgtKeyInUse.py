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
    print("파트너 관리번호 사용여부 확인")
    
    MgtKey = "111-1111-2222" #파트너 부여 세금계산서 관리번호, 1~24자리, 영문,숫자,-,_ 조합으로 공급자별 고유번호 생성

    bIsInUse = taxinvoiceService.checkMgtKeyInUse(testValue.testCorpNum,"SELL",MgtKey)
    print("사용여부 : %s" % "사용중" if bIsInUse else '미사용중')
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))