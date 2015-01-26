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
    print("세금계산서 정보 확인")
    
    MgtKeyType = "SELL" #관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "111-2222-3333"
 
    #세금계산서 임시저장시 구성한 정보를 반환한다.
    taxinvoice = taxinvoiceService.getDetailInfo(testValue.testCorpNum,MgtKeyType,MgtKey)

    #상태정보를 표시하기 위해 임의로 작성한 코드. 실재 변수처리시에는 taxinvoice.invoicerCorpNum, taxinvoice.detailList[0].itemName등으로 처리가능
    for key, value in taxinvoice.__dict__.items():
        if not key.startswith("__"):
            if key == 'detailList' or key == 'addContactList':
                print("%s :" % key)
                i = 1
                for t in value:
                    print("    %d:" % i)
                    for k, v in t.__dict__.items():
                        print("        %s : %s" % (k,v))
                    i += 1
            else:
                print("%s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))