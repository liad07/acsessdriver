from downloads import download
import os

acsess2010="https://download.microsoft.com/download/2/4/3/24375141-E08D-4803-AB0E-10F2E3A07AAA/AccessDatabaseEngine_X64.exe"
acsess2016="https://download.microsoft.com/download/3/5/C/35C84C36-661A-44E6-9324-8786B8DBE231/accessdatabaseengine_X64.exe"
download(acsess2010, out_path="acsess2010.exe")
download(acsess2016, out_path="acsess2016.exe")
os.system(f"acsess2010.exe /quiet")
os.system(f"acsess2016.exe /quiet")
os.system("shutdown -r")