from kivy.app import App
from kivy.lang import Builder


kv = Builder.load_string



class SettingScreen(App):

    def build(self):
        return kv


if __name__ == "__main__":
    SettingScreen().run()