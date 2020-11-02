import pandas as pd
import numpy as np

from datetime import datetime

allData = pd.read_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\2020.xlsx")


def try_parsing_date(text):
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    return datetime.now()


months = [try_parsing_date(str(date)[0:10]).month for date in allData["Дата оплаты"]]
allData["Месяц оплаты"] = np.array(months)
print(allData["Месяц оплаты"])

months = [try_parsing_date(str(date)[0:10]).month for date in allData["Дата подписания"]]
allData["Месяц подписи"] = np.array(months)
print(allData["Месяц подписи"])

year = [try_parsing_date(str(date)[0:10]).year for date in allData["Дата оплаты"]]
allData["Год оплаты"] = np.array(year)
print(allData["Год оплаты"])

indexNames = allData[allData["Год оплаты"] == 2019].index
allData.drop(indexNames , inplace=True)


def pars_org(text):
    if str(text)[0] == "Ф":
        return "ФЭЛ"
    
    if str(text)[0] == "Э":
        return "ЭН"

    return "Неизвестно"


allData["Организация"] = np.array([pars_org(number) for number in allData["Договор"]])

sortedByPayMonth = allData.sort_values(by=['Месяц оплаты'])
sortedByPayMonth.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\SortPayMonth.xlsx")

sortedBySignatureMonth = allData.sort_values(by=['Месяц подписи'])
sortedBySignatureMonth.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\SortSignatureMonth.xlsx")

FEL = allData[allData["Организация"] == "ФЭЛ"]
print(FEL)

sortedByPayMonth = FEL.sort_values(by=['Месяц оплаты'])
sortedByPayMonth.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\SortPayMonth_FEL.xlsx")

sortedBySignatureMonth = FEL.sort_values(by=['Месяц подписи'])
sortedBySignatureMonth.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\SortSignatureMonth_FEL.xlsx")

EN = allData[allData["Организация"] == "ЭН"]
print(EN)

sortedByPayMonth = EN.sort_values(by=['Месяц оплаты'])
sortedByPayMonth.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\SortPayMonth_EN.xlsx")

sortedBySignatureMonth = EN.sort_values(by=['Месяц подписи'])
sortedBySignatureMonth.to_excel("C:\\Users\\nadir\\Desktop\\Dahaster\\2020\\SortSignatureMonth_EN.xlsx")
