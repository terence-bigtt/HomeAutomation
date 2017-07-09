class MenuItem(object):
    def __init__(self, caption, page, target="_blank", id=0):
        self.caption = caption
        self.page = page
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
    item1 = MenuItem("Links", "general.links", id=1, target="include")
    item2 = MenuItem("Home", "general.index", id=2, target="include")
    menu = Menu(item1, item2)
    return menu
