class Link(object):
    def __init__(self, name, href, description="", id=0):
        self.name = name
        self.href = href
        self.description = description
        self.id = id


class Links(object):
    def __init__(self, *links):
        self.links = [l for l in links]

    def add_item(self, link):
        self.links.append(link)

    def remove_item(self, id):
        self.links = [it for it in self.items if it.id != id]


def get_configured_links():
    l1 = Link("Google", "http://www.google.com", "Your favorite search engine", id=0)
    l2 = Link("Photos", "http://teereence.quickconnect.to/photo", "Photos stored on the Nas", id=1)
    l3 = Link("Nas config", "http://teereence.quickconnect.to/", "Configurtion page for the Nas", id=2)

    return Links(l1, l2, l3)
