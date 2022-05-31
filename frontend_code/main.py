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
            "Blue bin": "images/news.png",
            " Blue bin ": "images/flyer.png",
            "  Blue bin  ": "images/magazine.png"
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
            "Garbage": "images/tissue.png",
            " Garbage ": "images/paper_towel.png",
            "  Garbage  ": "images/napkin.png"
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
            "Blue bin (no plastic lining)": "images/paper-bag.png",
            "Garbage (plastic lining)": "images/stand_bag.png"
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
            "Blue bin": "images/ad.png",
            " Blue bin ": "images/fine_paper.png",
            "  Blue bin  ": "images/envelope.png",
            "Garbage": "images/laminated_paper.png"
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
            "Blue bin (without inner lining)": "images/wax_cardboard.png",
            "Garbage (with inner lining)": "images/wax_cardboard.png",
            " Garbage ": "images/laminated_paper.png",
            "Blue bin": "images/wrapping_paper.png",
            " Blue bin ": "images/card.png",
            "   Blue bin   ": "images/bow.png"
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
            "Blue bin": "images/carton.png"
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
            "Garbage": "images/candy.png",
            " Garbage ": "images/chip.png",
            "Blue bin": "images/paper_bag.png",
            " Garbage ": "images/bubble_wrap.png",
            "  Blue bin  ": "images/ziploc_bag.png",
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
            "Blue bin": "images/bottle.png",
            " Blue bin ": "images/cap.jpg",
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
            "Garbage": "images/straw.png",
            " Garbage ": "images/stirrer.png",
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
            "Blue bin": "images/grocery.png",
            " Blue bin ": "images/milk.jpg",
            "  Blue bin  ": "images/frozen_food.png",
            "   Blue bin   ": "images/dry_clean.png",
            "    Blue bin    ": "images/soil.png",
            "Take to recycling plant": "images/tote.png"
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
            "Garbage": "images/cutlery.png",
            " Garbage ": "images/cutlery_black.png"
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
            "Blue bin": "images/shampoo.png",
            "Take empty bottle to retailer": "images/cosmetics.png"
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
            "Blue bin": "images/food_jar.png",
            "Garbage": "images/glass_bottle.png",
            " Garbage ": "images/perfume.png"
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
            "Garbage": "images/plate.png",
            " Garbage ": "images/drink_glass.png",
            "   Garbage   ": "images/bowl.png"
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
            "Garbage": "images/window_glass.png",
            " Garbage ": "images/facades.png"
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
            "Garbage": "images/mirror.png",
            " Garbage ": "images/light_bulb.png"
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
            "Bring to a drop off depot": "images/smartphone.png",
            " Bring to a drop off depot ": "images/tv.png"
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
            "Blue bin": "images/aluminum_can.png",
            " Blue bin ": "images/aluminum_tray.png",
            "  Blue bin  ": "images/cookie_tin.jpg",
            "   Blue bin   ": "images/cake_pan.jpg"
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
            "Blue bin (if empty and with lid on)": "images/spray_can.png",
            " Blue bin ": "images/paint_can.png",
            "Blue bin (paint lid recycled separately)": "images/paint_lid.png",
            "   Blue bin   ": "images/can.png"
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
            "Garbage": "images/aluminum_foil.png",
            " Garbage ": "images/chip_bag.png"
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

    def build(self):
        self.title = 'EnviroClean'
        return kv




MainApp().run()