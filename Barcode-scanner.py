import cv2
from pyzbar import pyzbar
import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image

def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start

def read_barcodes(frame):
#array of barcodes, decode frame which is camera
  barcodes = pyzbar.decode(frame)

  for barcode in barcodes:
   x,y,w,h = barcode.rect
  #in all the data find the 8 number code
   barcode_info = barcode.data.decode('utf-8')
  #cv2.rectangle(image, start_point coordinate, end_point, color, thickness)
   cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

  #make font
   font = cv2.FONT_HERSHEY_DUPLEX
  #write text on screen. cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
   cv2.putText(frame,"Scanned!", (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

   variable = barcode_info[1:]
   url = "https://www.barcodespider.com/" + variable
   headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
   page = requests.get(url,headers=headers)
   soup = BeautifulSoup(page.content, "html.parser")

   images = soup.find_all('img')
   alt = "upc " + variable + " product image"

   for img in images:
    if img.has_attr('alt'):
      if img['alt'] == alt:
        dataSrc = img['data-src']
        filename = "_SL150_.jpg"
        urllib.request.urlretrieve(dataSrc,filename)

        img = Image.open(filename)
        img.show()



  return frame

def main():

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #ret = boolean. checks whether or not there's return
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        #if escape key pressed, stop scanning
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
