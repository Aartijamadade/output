from zipfile import ZipFile

folder_path = "C:/Users/Dipak/Desktop/output"

zip_file_name = "output_1_0.zip"



z=ZipFile("Output_1_0.zip",'w')

z.write("zip.py")
z.write("test.py ")
z.write("text.txt")
z.write("test1.py")
z.write("text2.txt")
z.close()
