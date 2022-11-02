img_name = './002.zh-cht.png' : 調整載入的圖片 繁體中文


text = pytesseract.image_to_string(img, lang='chi_tra+eng') : 圖片轉文字，使用繁體中文與英文


英文 : eng


繁體中文 : chi_tra


簡體中文 : chi_sim


ocrText() : 將目標圖片轉換成文字


replaceText() : 依據需求替換指定文字


save() : 將文字保存到指定路徑


main() : 整體流程


取得 image 資料夾下所有的檔案名


使用 for in 逐筆轉換文字與處理檔名


轉換完成後，將文字保存到 text 資料夾
