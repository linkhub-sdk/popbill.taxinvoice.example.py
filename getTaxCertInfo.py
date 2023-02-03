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
팝빌 인증서버에 등록된 공동인증서의 정보를 확인합니다.
- https://developers.popbill.com/reference/taxinvoice/python/api/cert#GetTaxCertInfo
'''

try:
    print("=" * 15 + " 인증서 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    taxinvoiceCertificate = taxinvoiceService.getTaxCertInfo(CorpNum)

    print("인증서 정보>")
    print("regDT (등록일시) : %s " % taxinvoiceCertificate.regDT)
    print("expireDT (만료일시) : %s " % taxinvoiceCertificate.expireDT)
    print("issuerDN (인증서 발급자 DN) : %s " % taxinvoiceCertificate.issuerDN)
    print("subjectDN (등록된 인증서 DN) : %s " % taxinvoiceCertificate.subjectDN)
    print("issuerName (인증서 종류) : %s " % taxinvoiceCertificate.issuerName)
    print("oid (OID) : %s " % taxinvoiceCertificate.oid)
    print("regContactName (등록 담당자 성명) : %s " % taxinvoiceCertificate.regContactName)
    print("regContactID (등록 담당자 아이디) : %s " % taxinvoiceCertificate.regContactID)

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
