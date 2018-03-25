class MyProperty:
    def __init__(self):
        self._name = None
    def get_name(self):
        print("get_name called")
        return self._name
    def set_name(self, name):
        print("set_name called")
        self._name = name
    def del_name(self):
        print("del_name called")
        del self._name
    name = property(get_name, set_name, del_name, "'name' property.")

p = property()
p.name