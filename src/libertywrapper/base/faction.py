class FactionPenalty:
    def __init__(self, data):
        self.points = data.get("points")
        self.reason = data.get("reason")
        self.duration = data.get("duration")

    def repr(self):
        return f"FactionPenalty(points={self.points}, reason={self.reason}, duration={self.duration})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.points, self.reason, self.duration))

class BriefFaction:
    def __init__(self, name, faction_type=None, id=None, rank=None, **kwargs):
        self.name = name
        self.type = faction_type
        self.id = id
        self.rank = rank

    def repr(self):
        return f"Faction(name={self.name}, type={self.type}, id={self.id}, rank={self.rank})"
    
    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.name, self.type, self.id, self.rank))
    