import datetime

class ServerOnlineHistory:
    def __init__(self, data):
        self.date = datetime.datetime.strptime(data["date"], "%Y-%m-%d")
        self.players = data["maxOnline"]

    def repr(self):
        return f"ServerOnlineHistory(date={self.date}, players={self.players})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.date, self.players))

class JobEarnings:
    def __init__(self, **kwargs):
        self.miner = kwargs.get("miner")
        self.trucker = kwargs.get("trucker")
        self.fisherman = kwargs.get("fisherman")
        self.garbageman = kwargs.get("garbageman")
        self.lumberjack = kwargs.get("lumberjack")
        self.electrician = kwargs.get("electrician")

    def repr(self):
        return f"JobEarnings({self.__dict__})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.__dict__.items())
