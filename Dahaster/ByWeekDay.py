import pandas as pd
import numpy as np

from datetime import datetime

allData = pd.read_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\ФЭЛ+ЭН 2019.xlsx")

print(allData["Дата оплаты"])

def try_parsing_date(text):
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    return datetime.now()

weekdays = [try_parsing_date(str(date)[0:10]).weekday() for date in allData["Дата оплаты"]]
allData["День оплаты"] = np.array(weekdays)
print(allData["День оплаты"])

weekdays = [try_parsing_date(str(date)[0:10]).weekday() for date in allData["Дата подписи"]]
allData["День подписи"] = np.array(weekdays)
print(allData["День подписи"])

year = [try_parsing_date(str(date)[0:10]).year for date in allData["Дата оплаты"]]
allData["Год оплаты"] = np.array(year)
print(allData["Год оплаты"])

indexNames = allData[allData["Год оплаты"] == 2018].index
allData.drop(indexNames , inplace=True)

def pars_org(text):
    if (str(text)[0] == "Ф"):
        return "ФЭЛ"
    
    if (str(text)[0] == "Э"):
        return "ЭН"

    return "Неизвестно"

allData["Организация"] = np.array([pars_org(number) for number in allData["№ договора"]])

sorteByPayDay = allData.sort_values(by=['День оплаты'])
sorteByPayDay.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\WithWeekday_SortPayDay.xlsx")

sorteBySignatureDay = allData.sort_values(by=['День подписи'])
sorteBySignatureDay.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\WithWeekday_SortSignatureDay.xlsx")

FEL = allData[allData["Организация"] == "ФЭЛ"]

sorteByPayDay = FEL.sort_values(by=['День оплаты'])
sorteByPayDay.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\WithWeekday_SortPayDay_FEL.xlsx")

sorteBySignatureDay = FEL.sort_values(by=['День подписи'])
sorteBySignatureDay.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\WithWeekday_SortSignatureDay_FEL.xlsx")

EN = allData[allData["Организация"] == "ЭН"]

sorteByPayDay = EN.sort_values(by=['День оплаты'])
sorteByPayDay.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\WithWeekday_SortPayDay_EN.xlsx")

sorteBySignatureDay = EN.sort_values(by=['День подписи'])
sorteBySignatureDay.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\WithWeekday_SortSignatureDay_EN.xlsx")