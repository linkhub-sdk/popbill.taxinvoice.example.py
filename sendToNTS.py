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
[발행완료] 상태의 세금계산서를 국세청으로 즉시전송합니다.
- 국세청 즉시전송을 호출하지 않은 세금계산서는 발행일 기준 익일 오후 3시에 팝빌 시스템에서
  일괄적으로 국세청으로 전송합니다.
- 익일전송시 전송일이 법정공휴일인 경우 다음 영업일에 전송됩니다.
- 국세청 전송에 관한 사항은 "[전자세금계산서 API 연동매뉴얼] > 1.4 국세청 전송 정책" 을
  참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 국세청 즉시전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20161122-06"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.sendToNTS(CorpNum, MgtKeyType, MgtKey, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
