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
연동회원의 전자세금계산서 API 서비스 과금정보를 확인합니다.
- https://docs.popbill.com/taxinvoice/python/api#GetChargeInfo
'''

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = taxinvoiceService.getChargeInfo(CorpNum, UserID)

    tmp = "unitCost (발행단가) : " + response.unitCost + "\n"
    tmp += "chargeMethod (과금유형) : " + response.chargeMethod + "\n"
    tmp += "rateSystem (과금제도) : " + response.rateSystem

    print(tmp)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
