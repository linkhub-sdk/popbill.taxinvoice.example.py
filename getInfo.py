# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import Taxinvoice,TaxinvoiceDetail,Contact,TaxinvoiceService,PopbillException

taxinvoiceService =  TaxinvoiceService(testValue.LinkID,testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
  
try:
    print("세금계산서 상태 정보 확인")
    
    MgtKeyType = "SELL" #관리번호 유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKey = "111-2222-3333"
 
    taxinvoiceInfo = taxinvoiceService.getInfo(testValue.testCorpNum,MgtKeyType,MgtKey)

    ''' TaxinvoiceInfo 구성 : 항목별 자세한 내용은 매뉴얼 참조.
            itemKey                 
            stateCode               
            taxType                 
            purposeType             
            modifyCode              
            issueType               
            writeDate               

            invoicerCorpName        
            invoicerCorpNum         
            invoicerMgtKey          
            invoiceeCorpName        
            invoiceeCorpNum         
            invoiceeMgtKey          
            trusteeCorpName         
            trusteeCorpNum          
            trusteeMgtKey           

            supplyCostTotal         
            taxTotal                

            issueDT                 
            preIssueDT              
            stateDT                 
            openYN                  
            openDT                  

            ntsresult               
            ntsconfirmNum           
            ntssendDT               
            ntsresultDT             
            ntssendErrCode          
            stateMemo               

            regDT  
    '''
    #상태정보를 표시하기 위해 임의로 작성한 코드. 실재 변수처리시에는 taxinvoiceInfo.stateCode, taxinvoiceInfo.openYN등으로 처리가능
    for key, value in taxinvoiceInfo.__dict__.items():
        if not key.startswith("__"):
            print("%s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))