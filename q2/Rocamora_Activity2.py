class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def display_name(self):
        print(self.name)

    @display_name.setter
    def display_name(self, name):
        self.name = name

    @property
    def display_age(self):
        print(self.age)

    @display_age.setter
    def display_age(self, age):
        self.age = age

    @property
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
    

child1 = Child("Tinoy", 15)
child1.display    

class Grandfather:
    def __init__(self, grandfathername):
        self._grandfathername = grandfathername

    @property
    def grandfathername(self):
        return self._grandfathername

    @grandfathername.setter
    def grandfathername(self, name):
        self._grandfathername = name

    @property
    def display_grandfather(self):
        print("Grandfather name:", self._grandfathername)


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self._fathername = fathername

    @property
    def fathername(self):
        return self._fathername

    @fathername.setter
    def fathername(self, name):
        self._fathername = name

    @property
    def display_father(self):
        print("Father name:", self._fathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self._sonname = sonname

    @property
    def sonname(self):
        return self._sonname

    @sonname.setter
    def sonname(self, name):
        self._sonname = name

    @property
    def display(self):
        print("Grandfather name:", self.grandfathername)
        print("Father name:", self.fathername)
        print("Son name:", self.sonname)


brother = Son("Yan", "Ian", "Estiquo")
brother.display


class Child2(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
    


child2 = Child2("Ani", 21)
child2.display



