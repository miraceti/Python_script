import fnmatch
import os
# pth = "//172.16.10.7/info$/PROGRAMMATION/VBScripts/SATEC/DIAC/SFTP_TOUS/DIAC_20210203"
pth = "C:\Windows"
print(len(fnmatch.filter(os.listdir(pth), "*")))