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
1건의 전자명세서를 세금계산서에 첨부합니다.
- https://docs.popbill.com/taxinvoice/python/api#AttachStatement
'''

try:
    print("=" * 15 + " 전자명세서 첨부 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 세금계산서 문서번호
    MgtKey = "20210429-002"

    # 첨부할 전자명세서 종류코드, 121-명세서, 122-청구서, 123-견적서, 124-발주서 125-입금표, 126-영수증
    ItemCode = "121"

    # 첨부할 전자명세서 문서번호
    StmtMgtKey = "20190116-001"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.attachStatement(CorpNum, MgtKeyType, MgtKey, ItemCode,
                                               StmtMgtKey, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
