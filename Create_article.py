
import random

from openpyxl import load_workbook

class PostWriter():

    def readExcelFile(self, filepath):
            print("Read Phrase excel")
            load_wb = load_workbook(filepath)
            #시트 이름으로 불러오기
            load_ws = load_wb['문단']
            self.phList = [ [c.value for c in r]  for r in load_ws ]
            

            self.isLoaded = True

    def makeArticle(self):
        if(self.isLoaded):
            result = []
            for phs in self.phList:
                temp = None
                while(temp==None):
                    temp = random.choice(phs)

                result.append(temp)
            return result
        else:
            print("문단 엑셀 파일을 먼저 불러오세요.")
            return None
     
     
if __name__=="__main__":
    writer = PostWriter()
    writer.readExcelFile("./문단파일.xlsx")
    article = writer.makeArticle()

    print(article)
    
    with open("포스트.txt", "w", encoding="UTF-8") as wf:
        wf.write("\r\n".join(article))