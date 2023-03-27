import pandas as pd
import warnings
import openpyxl
from datetime import date


def filltering():
    warnings.simplefilter("ignore")
    global ts

    ex = pd.read_excel('/Users/sorang/Downloads/__')

    check_ok = ex['참여여부'] != '미참여'

    person_check = ex[check_ok]

    ts = person_check[['학년','반','번호','성명']]

    inventors = ts
    inventors.to_excel("/Users/sorang/Excel/일일확진자.xlsx", index = False)

def editsheet(i):
    wb = openpyxl.Workbook()

    # 날짜 설정
    tday = date.today()
    tday_s = tday.strftime('%b.%d')

    ws = wb.active
    ws["A1"] = '1'

    # 엑셀 저장 

    new_filename = '/Users/sorang/Excel/' + '일일확진자(' + tday_s + ').xlsx'
    wb.save(new_filename)



filltering()
editsheet(ts)