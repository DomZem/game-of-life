from UI.Component import Component


class Composite(Component):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def draw(self):
        for component in self.components:
            component.draw()