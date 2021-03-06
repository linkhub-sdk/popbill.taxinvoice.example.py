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

'''
세금계산서에 첨부된 파일을 삭제합니다.
- 첨부파일을 식별하는 파일아이디는 첨부파일 목록(GetFiles API) 함수의 응답항목
  중 파일아이디(AttachedFile) 통해 확인할 수 있습니다.
- https://docs.popbill.com/taxinvoice/python/api#DeleteFile
'''

try:
    print("=" * 15 + " 세금계산서 첨부파일 삭제 " + "=" * 15)

    # 팝빌회원 아이디
    CorpNum = testValue.testCorpNum

    # 세금계산서 발행유형, SELL : 매출 , BUY : 매입 , TRUSTEE : 수탁
    MgtKeyType = "SELL"

    # 문서번호
    MgtKey = "20190108-001"

    # 첨부파일 아이디, GetFiles API의 응답항목(AtachedFile) 확인.
    FileID = "AA5A49DC-8DBF-4F2D-B6ED-8AE84611058E.PBF"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    result = taxinvoiceService.deleteFile(CorpNum, MgtKeyType, MgtKey, FileID, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
