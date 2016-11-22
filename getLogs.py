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
세금계산서 상태 변경이력을 확인합니다.
- 상태 변경이력 확인(GetLogs API) 응답항목에 대한 자세한 정보는 "[전자세금계산서 API 연동매뉴얼]
  > 3.6.4 상태 변경이력 확인" 을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 상태변경 이력 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20161116-01"

    LogList = taxinvoiceService.getLogs(CorpNum, MgtKeyType, MgtKey)

    i = 1
    for f in LogList:
        print("%d : " % i)
        print("docLogType : %s" % f.docLogType)
        print("log : %s" % f.log)
        print("procType : %s" % f.procType)
        print("procCorpName : %s" % f.procCorpName)
        print("procMemo : %s" % f.procMemo)
        print("regDT : %s" % f.regDT)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
