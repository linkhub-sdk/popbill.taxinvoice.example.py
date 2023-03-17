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
파트너가 세금계산서 관리 목적으로 할당하는 문서번호의 사용여부를 확인합니다.
- 이미 사용 중인 문서번호는 중복 사용이 불가하고, 세금계산서가 삭제된 경우에만 문서번호의 재사용이 가능합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/info#CheckMgtKeyInUse
"""

try:
    print("=" * 15 + " 세금계산서 문서번호 사용여부 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호, 1~24자리, 영문,숫자,-,_ 조합으로 사업자별로 중복되지 않도록 구성
    MgtKey = "20220803-001"

    keyInUse = taxinvoiceService.checkMgtKeyInUse(CorpNum, MgtKeyType, MgtKey)

    print("문서번호 사용여부 : 사용중" if keyInUse else "문서번호 사용여부 : 미사용중")
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
