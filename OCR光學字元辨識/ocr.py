from PIL import Image
import pytesseract
import os
from os import listdir
from os.path import isfile, join


def ocrText(fileName):
    img = Image.open(fileName)
    # text = pytesseract.image_to_string(img, lang='eng')
    # text = pytesseract.image_to_string(img, lang='eng+chi_tra')
    text = pytesseract.image_to_string(img, lang='eng+chi_tra+chi_sim')
    return text


def replaceText(str):
    str = str.replace(",", "，")
    text = str.replace(" ", "")
    return text


def save(fileName, text):
    print("text.length => ", len(text))
    with open(fileName, 'w', encoding='UTF-8') as f:
        f.write(text)
        f.close


def main():
    path = '.' + os.sep + 'image'
    lstFile = [f for f in listdir(path) if isfile(join(path, f))]

    for f in lstFile:
        if '.png' in f:
            idx = f.find('.png')
            out_name = ""
            for i in range(idx):
                out_name += f[i]
            print(out_name)
            text = ocrText('.' + os.sep + 'image' + os.sep + '{}'.format(f))
            # text = replaceText(text)
            path = '.' + os.sep + 'text' + os.sep + out_name + '.txt'
            save(path, text)

def orc系統():
    import sys
    if sys.platform.startswith("linux"):
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/5.2.0/bin/tesseract"
    elif sys.platform == "darwin":
        # MAC OS X
        pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/5.2.0/bin/tesseract"
    elif sys.platform == "win32":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if __name__ == "__main__":
    orc系統()
    main()