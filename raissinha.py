from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
class MinhaApp(App):
    def build (self):
        return Label(
            text='Lulu te amo!!',font_size=100, font_name='Times', color=get_color_from_hex("#FF5733"),
            halign='left',        
            valign='top',
            size_hint=(None, None),
            size=(400, 400), 
            text_size=(None, None)                                                                                 
        )
if __name__ == "__main__":
    MinhaApp().run()