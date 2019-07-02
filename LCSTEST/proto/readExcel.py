# encoding : utf-8
import xlrd
class readExcel(object):
    def __init__(self,path):
        self.path=path

    @property
    def getSheet(self):
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    @property
    def getRows(self):
        row=self.getSheet.nrows
        return row

    @property
    def getCol(self):
       col = self.getSheet.ncols
       return col

    @property
    def getName(self):
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 0))
        return TestName

    @property
    def body(self):
        data=[]
        k=1
        while k <self.getRows:
            body = []
            for i in range(1, self.getCol):
                body.append(self.getSheet.cell_value(k, i))
            data.append(body)
            k+=1
        return data


