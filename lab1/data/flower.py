class Flower:
    def __init__(self, name, color, aroma, regions):
        self.name = name
        self.color = color
        self.aroma = aroma
        self.regions = regions

    def __gt__(self, other):
        if self.name != other.name:
            return self.name > other.name
        elif self.color != other.color:
            return self.color > other.color
        else:
            return self.aroma > other.aroma

    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        elif self.color != other.color:
            return self.color < other.color
        else:
            return self.aroma < other.aroma

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.color == other.color
            and self.aroma == other.aroma
        )
