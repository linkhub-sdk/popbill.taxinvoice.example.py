# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import PopbillException, TaxinvoiceService

taxinvoiceService = TaxinvoiceService(testValue.LinkID, testValue.SecretKey)
taxinvoiceService.IsTest = testValue.IsTest
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
세금계산서 상태 변경이력을 확인합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/info#GetLogs
"""

try:
    print("=" * 15 + " 세금계산서 상태변경 이력 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20220803-001"

    LogList = taxinvoiceService.getLogs(CorpNum, MgtKeyType, MgtKey)

    i = 1
    for f in LogList:
        print("%d : " % i)
        print("docLogType (로그타입) : %s" % f.docLogType)
        print("log (이력정보) : %s" % f.log)
        print("procType (처리형태) : %s" % f.procType)
        print("procCorpName (처리회사명) : %s" % f.procCorpName)
        print("procContactName (처리담당자) : %s" % f.procContactName)
        print("procMemo (처리메모) : %s" % f.procMemo)
        print("regDT (등록일시) : %s" % f.regDT)
        print("ip (아이피) : %s" % f.ip)
        print
        i += 1

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
