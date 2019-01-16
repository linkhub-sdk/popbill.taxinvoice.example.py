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

'''
1건의 세금계산서 상태/요약 정보를 확인합니다.
- 세금계산서 상태정보(GetInfo API) 응답항목에 대한 자세한 정보는 "[전자세금계산서 API 연동매뉴얼]
  > 4.2. (세금)계산서 상태정보 구성" 을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 상태/요약 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20190116-001"

    taxinvoiceInfo = taxinvoiceService.getInfo(CorpNum, MgtKeyType, MgtKey)

    # 상태정보를 표시하기 위해 임의로 작성한 코드.
    # 실제 변수처리시에는 taxinvoiceInfo.stateCode, taxinvoiceInfo.openYN등으로 처리가능
    for key, value in taxinvoiceInfo.__dict__.items():
        if not key.startswith("__"):
            print("%s : %s" % (key, value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
