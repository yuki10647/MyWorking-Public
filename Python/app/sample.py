# coding utf-8
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget    # 自分でカスタム

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint

#フォント変更
# resource_add_path('C:\Windows\Fonts')
# LabelBase.register(DEFAULT_FONT, 'PingFang.ttc')

# resource_add_path('./shot')  あっても駄目だった

class ImageWidget(Widget):  #　全体のカスタム
    source = StringProperty('shot/image1.png')

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonStarted(self):
        self.source = 'shot/image1.png'
    
    def buttonRandom(self):
        self.source = f'shot/image{randint(1, 4)}.png'

class SampleApp(App):
    def __init__(self, **kwargs):
        super(SampleApp, self).__init__(**kwargs)
        self.title = 'screen'

if __name__=='__main__':
    SampleApp().run()





