import xlrd
import os
import ReadConfig 


class Xlrd:
    def __init__(self,):
        proDir = ReadConfig.proDir
        readconfig=ReadConfig.ReadConfig()
        xls_name = readconfig.get_xls('xls_name')
        sheet_name = readconfig.get_xls('sheet_name')
        xlsPath = os.path.join(proDir,'testfile',xls_name)
        file = xlrd.open_workbook(xlsPath)
        self.sheet = file.sheet_by_name(sheet_name)
        self.row = self.sheet.row_values(0)
        self.rowNum  = self.sheet.nrows
        self.colNum = self.sheet.ncols 

    def get_xls(self):
        cls = []
        for i in range(self.rowNum):
            if self.sheet.row_values(i)[0] !=u'case_name':
                cls.append(self.sheet.row_values(i))
        return cls

    def get_xls_next(self):
        cls = []
        curRowNo = 1
        while self.hasNext(self.rowNum,curRowNo):
            s = {}  
            col = self.sheet.row_values(curRowNo)  
            i = self.colNum  
            for x in range(i):  
                s[self.row[x]] = col[x]  
            cls.append(s)  
            curRowNo += 1 
        return cls


    def hasNext(self,rownum,curRowNo):  
        if rownum == 0 or rownum <= curRowNo :  
            return False  
        else:  
            return True  
