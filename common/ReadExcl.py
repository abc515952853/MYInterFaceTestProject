import xlrd
import os
import ReadConfig 


class Xlrd:
    def __init__(self,):
        proDir = ReadConfig.proDir
        readconfig=ReadConfig.ReadConfig()
        xls_name = readconfig.get_xls('xls_name')
        xlsPath = os.path.join(proDir,'testfile',xls_name)
        self.file = xlrd.open_workbook(xlsPath)

    #获取sheet列名
    def get_sheet_colname(self,sheet_name):
        sheet = self.file.sheet_by_name(sheet_name)
        row = sheet.row_values(0)
        colNum = sheet.ncols 

        cls = {}
        for i in range(colNum):
            cls[sheet.row_values(0)[i]]=i
        return cls
    

    #遍历sheet中的用例
    def get_xls_next(self,sheet_name):
        sheet = self.file.sheet_by_name(sheet_name)
        row = sheet.row_values(0)
        rowNum  = sheet.nrows
        colNum = sheet.ncols 
        
        cls = []
        curRowNo = 1
        while self.hasNext(rowNum,curRowNo):
            s = {}  
            col = sheet.row_values(curRowNo)  
            i = colNum  
            for x in range(i):
                s[row[x]] = self.conversion_cell(sheet,curRowNo,x,col[x])
            cls.append(s)  
            curRowNo += 1
        return cls

    def hasNext(self,rownum,curRowNo):  
        if rownum == 0 or rownum <= curRowNo :  
            return False  
        else:  
            return True  
    #将读取excl整形的float，转换成int
    def conversion_cell(self,sheet,curRowNo,curColNo,cell):
        #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error  
        if sheet.cell(curRowNo,curColNo).ctype == 2:
             no =  int(cell)
        else:
             no = cell
        return no
            
        