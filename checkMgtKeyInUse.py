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
taxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
taxinvoiceService.UseStaticIP = testValue.UseStaticIP
taxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
세금계산서 관리번호 중복여부를 확인합니다.
- 관리번호는 1~24자리로 숫자, 영문 '-', '_' 조합으로 구성할 수 있습니다.
- https://docs.popbill.com/taxinvoice/python/api#CheckMgtKeyInUse
'''

try:
    print("=" * 15 + " 세금계산서 문서번호 사용여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
    MgtKey = "20190108-001"

    keyInUse = taxinvoiceService.checkMgtKeyInUse(CorpNum, MgtKeyType, MgtKey)

    print("문서번호 사용여부 : 사용중" if keyInUse else "문서번호 사용여부 : 미사용중")
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
