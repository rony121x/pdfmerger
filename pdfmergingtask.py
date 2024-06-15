import os
from PyPDF2 import PdfMerger
from PyPDF2 import *
# import pathlib

print(os.getcwd())
try:
    os.mkdir("OUTPUT")
except:
    pass  

pdfs=[]
allpdfs=[]
list_files = [file for file in os.listdir(f"{os.getcwd()}/INPUT") if file.endswith(".pdf")]
for file in list_files:
    # if file.strip().split(".")[-1]:
    f = file
# print("file location", filelocation)


# for f in filelocation.glob("*.pdf"):
    print(f)
    c=-1
    f=os.path.basename(f)
    allpdfs.append(f)
    
    for f1 in f:
        c+=1
        
        if f1.isdigit() and f[c-1]=="_" and f[c+1]=="_":
            trimmed=f[:c]+f[c+2:]
            pdfs.append(trimmed)
         
            
for x in pdfs:
    merger=PdfMerger()
    for y in list_files:
        y=os.path.basename(y)
        
        b=-1
        for y1 in y:
            b+=1
            
            if y1.isdigit() and y[b-1]=="_" and y[b+1]=="_":
                trimmed1=y[:b]+y[b+2:]
                if trimmed1==x:
                    r=open(f"{os.getcwd()}/INPUT/{y}","rb")
                    reader=PdfReader(r)
                    merger.append(reader)
                    
    with open(f"OUTPUT\\{x}","wb") as newfile:
        
        merger.write(newfile)                    
                    
    
      
                   
                    
            
                                
    
       
            
            
            
            
            



        
        

