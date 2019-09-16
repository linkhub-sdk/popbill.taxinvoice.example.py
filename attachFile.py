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

'''
세금계산서에 첨부파일을 등록합니다.
- [임시저장] 상태의 세금계산서만 파일을 첨부할수 있습니다.
- 첨부파일은 최대 5개까지 등록할 수 있습니다.
'''

try:
    print("=" * 15 + " 세금계산서 파일첨부 " + "=" * 15)

    # 팝빌회원 아이디
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서관리번호
    MgtKey = "20190108-002"

    # 파일경로
    FilePath = "test.jpeg"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.attachFile(CorpNum, MgtKeyType, MgtKey, FilePath, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
