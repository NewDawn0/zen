from random import randint
from threading import Thread
from time import sleep

from textual.app import App
from textual.reactive import reactive
from textual.widgets import Static

DA_NUMBA = "Hello"

strings = ["Hello", "World", "What", "The", "FUCK", "Is", "This", "So", "Bad", "To"]


def set_da_numba():
    global DA_NUMBA
    while True:
        sleep(0.1)
        DA_NUMBA = strings[randint(0, 9)]


def gen_da_thread():
    thread = Thread(target=set_da_numba)
    thread.daemon = True
    thread.start()


BUF_REF = None


def test():
    while True:
        sleep(1)
        BUF_REF.update_text(f"{DA_NUMBA}")


class TextBuf(Static):
    text = reactive("hello")

    def on_mount(self):
        gen_da_thread()
        global BUF_REF
        BUF_REF = self
        thread = Thread(target=test)
        thread.daemon = True
        thread.start()

    def update_text(self, text):
        self.text = text
        self.update(text)

    def render(self):
        return self.text


class Main(App):
    def compose(self):
        yield TextBuf()


Main().run()
