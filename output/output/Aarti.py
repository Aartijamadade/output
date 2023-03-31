from zipfile import ZipFile

z=ZipFile("Output_1_0.zip",'w')

z.write("zip.py")
z.write("test.py")
z.write("text.txt")
z.close()