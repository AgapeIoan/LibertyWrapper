class FactionInteriorGeneral:
    def __init__(self, data):
        self.heading = data.get("heading")
        self.position = tuple(data.get("position").values())

    def repr(self):
        return f"FactionInteriorGeneral(heading={self.heading}, position={self.position})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.heading, self.position))

class FactionInteriorHQ(FactionInteriorGeneral):
    def __init__(self, data):
        super().__init__(data)
        self.duty_pos = tuple(data.get("dutyPos").values())
        self.ipl_list = data.get("IPLList")

    def repr(self):
        return f"FactionInterior(ipl_list={self.ipl_list}, duty_pos={self.duty_pos}, heading={self.heading}, position={self.position})"

    def __iter__(self):
        return iter((self.ipl_list, self.duty_pos, self.heading, self.position))

class FactionInteriorGarage(FactionInteriorGeneral):
    def __init__(self, data):
        super().__init__(data)
        self.ipl_list = data.get("IPLList")

    def repr(self):
        return f"FactionInterior(ipl_list={self.ipl_list}, heading={self.heading}, position={self.position})"

    def __iter__(self):
        return iter((self.ipl_list, self.heading, self.position))

class FactionGarage:
    def __init__(self, data):
        self.hq = tuple(data.get("HQ").values())
        self.exit = FactionInteriorGeneral(data.get("Exit"))
        self.enter = FactionInteriorGeneral(data.get("Enter"))
        self.interior = FactionInteriorGarage(data.get("Interior"))

    def repr(self):
        return f"FactionGarage(hq={self.hq}, exit={self.exit}, enter={self.enter}, interior={self.interior})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.hq, self.exit, self.enter, self.interior))
