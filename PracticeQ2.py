class PSHS_Galaxy:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name
        else:
            print("Name cannot be empty.")


class Nationalities(PSHS_Galaxy):
    def __init__(self, name, country_code):
        super().__init__(name)
        self.country_code = country_code


class Filipino(Nationalities):
    def __init__(self):
        super().__init__(name="Philippines", country_code="PH")


class Spaniard(Nationalities):
    def __init__(self):
        super().__init__(name="Spain", country_code="ES")

class Indonesian(Nationalities):
    def __init__(self):
        super().__init__(name="Indonesia", country_code="ID")


class Aliens(PSHS_Galaxy):
    def __init__(self, name, powers):
        super().__init__(name)
        self.powers = powers


class Avengers(Aliens):
    def __init__(self, powers=None):
        super().__init__(name="Avengers", powers=powers if powers else [])


solarSystemOne = PSHS_Galaxy("Sol")
print("Galaxy Entity:", solarSystemOne.name)

Juan = Filipino()
print(f"Nationality: {Juan.name} (Code: {Juan.country_code})")

Loki = Avengers(powers=["Asgardian God", "Duplication", "Illusions", "Shapeshifting"])
print(f"Alien: {Loki.name}, Powers: {Loki.powers}")