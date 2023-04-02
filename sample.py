import os

folder_path = "C:/Users/Dipak/Desktop/abc" 

files = os.listdir(folder_path)


files=[os.path.join(folder_path,f)for f in files]

files.sort(key=lambda x:
           
           os.path.getmtime(x),reverse=true)

for f in files:
    print(f)
