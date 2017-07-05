from jinja2 import Undefined
class MenuItem(object):
    def __init__(self, caption, href, target="_blank", id=0):
        self.caption = caption
        self.href = href
        self.target = target
        self.id = id


class Menu(object):
    def __init__(self, *items):
        self.items = [it for it in items]

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, id):
        self.items = [it for it in self.items if it.id != id]


def get_configured_menu():
    item1 = MenuItem("Google", "http://www.google.com", id=1)
    item2 = MenuItem("Home", "/", id=2, target="iframe")
    menu = Menu(item1, item2)
    return menu
