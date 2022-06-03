
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
import cv2
from pyzbar import pyzbar
import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image


class ScreenOne(Screen, TabbedPanel):
    pass
class ScreenTwo(Screen):
    pass
class ScreenMLModel(Screen):
    pass
class ScreenThree(Screen):
    pass
class ScreenFour(Screen):
    pass
class ScreenFive(Screen):
    pass
class ScreenSix(Screen):
    pass
class ScreenSeven(Screen):
    pass
class ScreenEight(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class MyLayout(TabbedPanel):
    background_color = (0, 1, 0, .5)
    def build(self):
        pass

class TouchApp(App):
    def build(self):
        return Screen()

class MainApp(MDApp):
    def callback_for_menu_items(self, *args):
        toast(args[0])

    def grid_bottom_sheet_newspaper(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Newspaper": "images/news.png",
            "Blue bin: Flyers": "images/flyer.png",
            "Blue bin: Magazines": "images/magazine.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def grid_bottom_sheet_paper_towel(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Tissue": "images/tissue.png",
            "Garbage: Paper towels": "images/paper_towel.png",
            "Garbage: Napkins": "images/napkin.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def grid_bottom_sheet_bag(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Paper bags with no plastic lining": "images/paper-bag.png",
            "Garbage: Bags with plastic lining": "images/stand_bag.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def grid_bottom_sheet_mail(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Mail ads": "images/ad.png",
            "Blue bin: Printer paper": "images/fine_paper.png",
            "  Blue bin: Envelopes  ": "images/envelope.png",
            "Garbage: Laminated paper": "images/laminated_paper.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_gift_wrap(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Boxes without inner lining": "images/wax_cardboard.png",
            "Garbage: Boxes with inner lining": "images/wax_cardboard.png",
            " Garbage: Shiny wrapping paper ": "images/laminated_paper.png",
            "Blue bin: Non-shiny wrapping paper": "images/wrapping_paper.png",
            " Blue bin: Cards ": "images/card.png",
            "   Blue bin: Bows   ": "images/bow.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_cartons(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Milk cartons": "images/carton.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def grid_bottom_sheet_wrappers(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Candy wrappers": "images/candy.png",
            " Garbage: Chip bags": "images/chip.png",
            "Blue bin: Paper bags": "images/paper_bag.png",
            " Garbage: Bubble wrap ": "images/bubble_wrap.png",
            "  Blue bin: Ziploc bags  ": "images/ziploc_bag.png",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_bottles_caps(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Bottles with caps on": "images/bottle.png",
            " Blue bin: Bottle caps ": "images/cap.jpg",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_straws_stoppers(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Straws": "images/straw.png",
            " Garbage: Stirrers ": "images/stirrer.png",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_bags(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Grocery bags": "images/grocery.png",
            " Blue bin: Milk bags ": "images/milk.jpg",
            "  Blue bin: Frozen food bags  ": "images/frozen_food.png",
            "   Blue bin: Dry cleaning bags   ": "images/dry_clean.png",
            "    Blue bin: Soil bags    ": "images/soil.png",
            "Take to recycling plant: Tote bags": "images/tote.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_cutlery(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: White cutlery": "images/cutlery.png",
            " Garbage: Black cutlery ": "images/cutlery_black.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_shampoo(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Shampoo bottle": "images/shampoo.png",
            "Take empty bottle to retailer: Cosmetics": "images/cosmetics.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_packaging(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Food jar": "images/food_jar.png",
            "Garbage: Milk bottles": "images/glass_bottle.png",
            " Garbage: Perfume bottles ": "images/perfume.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_tableware(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Ceramic plates": "images/plate.png",
            " Garbage: Drinking glasses ": "images/drink_glass.png",
            "   Garbage: Bowls   ": "images/bowl.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_housing(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Window glass": "images/window_glass.png",
            " Garbage: Facades ": "images/facades.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_interior_design(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Mirrors": "images/mirror.png",
            " Garbage: Light bulbs ": "images/light_bulb.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_electronics(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Bring to a drop off depot: Old smartphones": "images/smartphone.png",
            " Bring to a drop off depot: Old TVs ": "images/tv.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_food_products(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Aluminum cans": "images/aluminum_can.png",
            " Blue bin: Aluminum trays ": "images/aluminum_tray.png",
            "  Blue bin: Cookie tins ": "images/cookie_tin.jpg",
            "   Blue bin: Cake pans   ": "images/cake_pan.jpg"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_cans(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Blue bin: Spray cans (if empty and with lid on)": "images/spray_can.png",
            " Blue bin: Paint cans ": "images/paint_can.png",
            "Blue bin: Paint lid": "images/paint_lid.png",
            "   Blue bin: Cans   ": "images/can.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_foil(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: Aluminum foil": "images/aluminum_foil.png",
            " Garbage: Chip bags (with inner lining) ": "images/chip_bag.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def grid_bottom_sheet_food_waste(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Green bin: fruit cores": "images/core.png",
            "Green bin: meat and bones": "images/meat.png",
            "Green bin: grains and rice products": "images/wheat-flour.png",
            "Green bin: dairy products": "images/dairy-products.png",
            "Green bin: baked goods": "images/sweets.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_napkins_towels(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Green bin: clean napkins": "images/napkin.png",
            "Green bin: clean paper towels": "images/brown-paper-towel.png",
            "Green bin: used napkins/paper towels": "images/used-napkin.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_food_container(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Green bin: dirty pizza boxes": "images/pizza-box.png",
            "Green bin: dirty paper plates": "images/dirty_plate.png",
            "Green bin: paper cupcake cups": "images/cupcake.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_waste(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Green bin: pet waste": "images/pawprint.png",
            "Green bin: diapers": "images/baby-diaper.png",
            "Garbage: menstruation products": "images/sanitary-pad.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def grid_bottom_sheet_disposable_safety_items(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: disposable masks": "images/mask.png",
            "Garbage: disposable gloves": "images/rubber-gloves.png",
            "Garbage: disposable gowns": "images/gown.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_soiled_items(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: soiled dressing": "images/gown.png",
            "Garbage: soiled sponges": "images/sponge.png",
            "Garbage: soiled gauze": "images/bandage.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def grid_bottom_sheet_hospital_clinic_items(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Garbage: catheters and colostomy bags": "images/catheter.png",
            "Garbage: IV bags & tubing": "images/iv-bag.png",
            "Garbage: dialysis waste": "images/dialysis.png"
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()

    def find_nth(haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start + len(needle))
            n -= 1
        return start

    def read_barcodes(self, frame):
        # array of barcodes, decode frame which is camera
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            x, y, w, h = barcode.rect
            # in all the data find the 8 number code
            barcode_info = barcode.data.decode('utf-8')
            # cv2.rectangle(image, start_point coordinate, end_point, color, thickness)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # make font
            font = cv2.FONT_HERSHEY_DUPLEX
            # write text on screen. cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
            cv2.putText(frame, "Scanned!", (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

            variable = barcode_info[1:]
            url = "https://www.barcodespider.com/" + variable
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")

            images = soup.find_all('img')
            alt = "upc " + variable + " product image"

            for img in images:
                if img.has_attr('alt'):
                    if img['alt'] == alt:
                        dataSrc = img['data-src']
                        filename = "_SL150_.jpg"
                        urllib.request.urlretrieve(dataSrc, filename)

                        img = Image.open(filename)
                        img.show()

        return frame

    def main(self):
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # ret = boolean. checks whether or not there's return
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame = self.read_barcodes(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            # if escape key pressed, stop scanning
            if cv2.waitKey(1) & 0xFF == 27:
                break

        camera.release()
        cv2.destroyAllWindows()

    def build(self):
        self.title = 'EnviroClean'
        return kv


MainApp().run()