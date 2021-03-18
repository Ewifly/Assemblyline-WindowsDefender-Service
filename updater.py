#  get new Security intelligence updates 

import requests
import os
from util import downloadBigFile
import subprocess
from bs4 import BeautifulSoup
import re

mpEngineExists =  os.path.isfile(os.path.join("engine","mpengine.dll"))

boolDownloadLatestVersion = False

strProductVersionNumberLocal = ""
strProductVersionNumberRemote = ""

if mpEngineExists:
    ps = subprocess.Popen(('exiftool', 'engine/mpengine.dll'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('grep', 'Product Version Number'), stdin=ps.stdout)
    ps.wait()
    strProductVersionNumberLocal =  str(output).split(':')[1]

    print("Local product version number = %s " % strProductVersionNumberLocal)

    print("Getting remote production version number...")

    url="https://www.microsoft.com/en-us/wdsi/defenderupdates"

    html_content = requests.get(url).text
  
    strProductVersionNumberRemote  = re.findall("<li>Engine Version.*?<span>(.*?)</span></li>", html_content)[0]
    print("Remote engine version number is %s " % strProductVersionNumberRemote )
  

    if(strProductVersionNumberRemote in strProductVersionNumberLocal):
        print("Local version == remote version, not updating")
    else:
        print("Remote version <> local")
        boolDownloadLatestVersion = True
else:   
        print("Nothing downloaded yet.")
        boolDownloadLatestVersion = True

if(boolDownloadLatestVersion):
    print("Downloading %s ... " % 'https://go.microsoft.com/fwlink/?LinkID=121721&arch=x86' )

    downloadBigFile("https://go.microsoft.com/fwlink/?LinkID=121721&arch=x86", "./engine/mpam-fe.exe" )

    print("Extracting mpam-fe.exe with cabextract ... ")

    os.system("cd engine && cabextract mpam-fe.exe")







