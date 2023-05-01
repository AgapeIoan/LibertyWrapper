import datetime

class GenericUser:
    def __init__(self, **kwargs):
        self.avatar = kwargs.get("UserAvatar")
        self.name = kwargs.get("name")
        self.level = kwargs.get("Level")
        self.playtime = datetime.timedelta(seconds=kwargs.get("Playtime", 0))
    
    def repr(self):
        return f"User(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.avatar, self.name, self.level, self.playtime))

class FactionUser:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.level = kwargs.get("Level")
        self.faction_rank = kwargs.get("FactionRank")
        self.user_avatar = kwargs.get("UserAvatar")

    def repr(self):
        return f"FactionUser(id={self.id}, name={self.name}, level={self.level}, faction_rank={self.faction_rank}, user_avatar={self.user_avatar})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.id, self.name, self.level, self.faction_rank, self.user_avatar))
