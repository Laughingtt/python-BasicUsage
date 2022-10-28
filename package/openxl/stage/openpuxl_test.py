import openpyxl
from openpyxl import load_workbook

wb = openpyxl.Workbook()
ws = wb.active

name = ["tian", "jian", "as", "dd"]
age = [20, 7, 20, 8]
sex = ["boy", "girl", "boy", "girl"]
ws.append(["name", "age", "sex"])
for i in range(len(name)):
    ws.append([name[i], age[i], sex[i]])

wb.save("xlsx练习.xlsx")
