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
1건의 세금계산서 상세항목을 확인합니다.
- 응답항목에 대한 자세한 사항은 "[전자세금계산서 API 연동매뉴얼]  > 4.1 (세금)계산서 구성" 을
  참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형 , SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서 관리번호
    MgtKey = "20161122-06"

    taxinvoice = taxinvoiceService.getDetailInfo(CorpNum, MgtKeyType, MgtKey)

    # 상태정보를 표시하기 위해 임의로 작성한 코드.
    # 실제 변수처리시에는 taxinvoice.invoicerCorpNum, taxinvoice.detailList[0].itemName등으로 처리가능
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
