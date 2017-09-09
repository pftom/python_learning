from xlrd import open_workbook

import json


wb = open_workbook('cooperation.xls')
table = wb.sheets()[0]

print(table.row_values(1)[3])

finally_data = {
    2: "firmName",
    6: "personName",
    7: "personPhone",
    10: "firmPhone",
    11: "address",
}
filter_items = [2, 6, 7, 10, 11]
total_items = []


for i in range(2, table.nrows):
    data_item = {}

    for j in range(12):
        if j in filter_items:
            if table.row_values(i)[j]:
                data_item[finally_data[j]] = table.row_values(i)[j]
            else:
                data_item[finally_data[j]] = '暂无'
    data_item['key'] = str(i)
    total_items.append(data_item)


with open('cooperation.json', 'w') as f_obj:
    f_obj.write(str(total_items))