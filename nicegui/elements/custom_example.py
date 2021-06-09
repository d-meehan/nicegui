import os.path
from .custom_view import CustomView
from .element import Element

class CustomExampleView(CustomView):

    vue_type = 'custom_example'
    vue_filepath = os.path.realpath(__file__).replace('.py', '.js')

    def __init__(self, on_change):

        self.on_change = on_change

        super().__init__(value=0)
        self.allowed_events = ['onAdd']
        self.initialize(temp=False, onAdd=self.handle_add)

    def handle_add(self, msg):

        self.options.value += msg.number
        self.on_change(self.options.value)

class CustomExample(Element):

    def __init__(self, *, on_change):

        super().__init__(CustomExampleView(on_change))

    def add(self, number: str):

        self.view.options.value += number
        self.view.on_change(self.view.options.value)
