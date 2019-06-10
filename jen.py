import xlwt
from xlwt import Workbook
import xml.etree.ElementTree as ET

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
tree = ET.parse('config.xml')
root = tree.getroot()
callevent = root.find('rolemap')
Moc1 = callevent.findall('role')
i=0
for moc in Moc1:
    for key, val in moc.items():
        if key == 'name':
            print(str(val))
            sheet1.write(i, 0, str(val))
        if key == 'pattern':
            sheet1.write(i, 1, str(val))
    for node in moc.getiterator():

        if node.tag == 'sid':
            print(node.text)
            sheet1.write(i, 2, node.text)
            i=i+1
wb.save("xlwt_example.xls")
