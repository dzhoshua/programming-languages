from enum import Enum


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.add_child(self)

    def add_child(self, child: "Widget"):
        if child not in self.children:
            self.children.append(child)
    
    def __str__(self):
        return f"{self.__class__.__name__}{self.children}"

    def __repr__(self):
        return str(self)
    

    def to_binary(self):
        res  = {
            "class_name": self.__class__.__name__,
            "children":[child.to_binary() for child in self.children]
        }

        if isinstance(self, Layout):
            res["alignment"] = self.alignment.value
        elif isinstance(self, LineEdit):
            res["max_length"] = self.max_length
        elif isinstance(self, ComboBox):
            res["items"] = self.items
        elif isinstance(self, MainWindow):
            res["title"] = self.title

        return res

    @classmethod
    def from_binary(cls, data, parent=None):
        class_name = data["class_name"]
        
        root_element = None
        if class_name == "MainWindow":
            root_element = cls(data["title"])
        elif class_name == "Layout":
            root_element = Layout(parent, data["alignment"])
        elif class_name == "LineEdit":
            root_element = LineEdit(parent, data["max_length"])
        elif class_name == "ComboBox":
            root_element = ComboBox(parent, data["items"])

        for child_data in data["children"]:
            child_node = cls.from_binary(child_data, parent=root_element)
            root_element.add_child(child_node)

        return root_element



class MainWindow(Widget):

    def __init__(self, title: str):
        super().__init__(None)
        self.title = title


class Layout(Widget):

    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment


class LineEdit(Widget):

    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length


class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items


app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(app)

bts = app.to_binary()
print(f"Binary data length {len(bts)}")
#print(bts)

new_app = MainWindow.from_binary(bts)
print(new_app)

print(new_app.children[1].children[1].items)
