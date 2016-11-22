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
팝빌 전자세금계산서 관련 문서함 팝업 URL을 반환합니다.
- 보안정책으로 인해 반환된 URL의 유효시간은 30초입니다.
'''

try:
    print("=" * 15 + " 세금계산서 문서함 팝업 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # SBOX : 매출보관함, PBOX : 매입보관함 , TBOX : 임시문서함 , WRITE : 문서작성
    TOGO = "WRITE"

    url = taxinvoiceService.getURL(CorpNum, UserID, TOGO)
    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
