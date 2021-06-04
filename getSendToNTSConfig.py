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
국세청 전송 설정 확인
- https://docs.popbill.com/taxinvoice/python/api#GetSendToNTSConfig
'''

try:
    print("=" * 15 + " 국세청 전송 설정 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    sendToNTSConfig = taxinvoiceService.getSendToNTSConfig(CorpNum)

    print("sendToNTS: %s" % sendToNTSConfig)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
