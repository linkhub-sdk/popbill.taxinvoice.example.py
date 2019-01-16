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
1건의 [임시저장] 상태의 세금계산서를 [발행예정] 처리합니다.
- 발행예정이란 공급자와 공급받는자 사이에 세금계산서 확인 후 발행하는 방법입니다.
- "[전자세금계산서 API 연동매뉴얼] > 1.2.1. 정발행 > 다. 임시저장 발행예정" 의 프로세스를 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 발행예정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20190108-001"

    # 메모
    Memo = "발행예정 메모"

    # 안내메일 제목, 미기재시 기본양식으로 전송
    EmailSubject = ""

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.send(CorpNum, MgtKeyType, MgtKey, Memo, EmailSubject, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
