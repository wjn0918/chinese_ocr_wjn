#-*- coding:utf-8 -*-
import os
import time
import numpy as np
from PIL import Image
import textract
import requests


SUFFIX1 = ['doc','docx','pdf']
SUFFIX2 = ['png', 'jpg']

files = '/var/lib/tomcat8/webapps/ROOT/'


def downloadFile(file_url, suffix):
    """
    download file
    :@return filePath: local file path
    """
    filedir = files + str(suffix)
    fileName = file_url.split('/')[-1]

    if os.path.exists(filedir):
        filePath = filedir + '/' + fileName
    else:
        os.mkdir(filedir)
        filePath = filedir + '/' + fileName

    r = requests.get(file_url)
    with open(filePath, "wb") as fw:
        fw.write(r.content)
    return filePath 





def chineseOCR(filePath):
    return textract.process(filePath, method='tessract', language='chi_sim', psm=5)



def recognition(fileUrl):
    """
    execute file recognition
    """
    suffix = fileUrl.split('.')[-1]
    filePath = downloadFile(fileUrl, suffix)
    if suffix in SUFFIX1:
        return textract.process(filePath)
    elif suffix in SUFFIX2:
        return chineseOCR(filePath).replace(" ", "")
    else:
        return ""
