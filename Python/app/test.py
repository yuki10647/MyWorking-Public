#   https://kivy.org/doc/stable/#
# kv ファイルは App() の前のTest をもちいて test.kv とする必要がある


from kivy.app import App
# from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# resource_add_path('C:\Windows\Fonts') # Mac /System/Library/Fonts
# LabelBase.register(DEFAULT_FONT, 'HGS明朝E')

class TestApp(App):    # 継承
    pass

# App().run()
if __name__=='__main__':
    TestApp().run()
