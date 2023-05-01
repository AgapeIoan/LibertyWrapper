from .user import GenericUser
from .base.faction import BriefFaction

class UserActivity(GenericUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.faction = BriefFaction(kwargs.get("Faction").get("name")) if kwargs.get("Faction") else None

    def repr(self):
        return f"UserActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, faction={self.faction})"

    def __iter__(self):
        pass

class UserQuestsActivity(GenericUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.quests = DailyQuests(kwargs.get("DailyQuestsStats")) if kwargs.get("DailyQuestsStats") else None

    def repr(self):
        return f"UserQuestsActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, quests={self.quests})"

    def __iter__(self):
        return super().__iter__()

class UserJobsActivity(GenericUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.money = kwargs.get("money")

    def repr(self):
        return f"UserJobsActivity(avatar={self.avatar}, name={self.name}, level={self.level}, playtime={self.playtime}, id={self.id}, money={self.money})"

    def __iter__(self):
        pass

class DailyQuests:
    def __init__(self, quests):
        self.streak = quests.get("streak")
        self.completed = quests.get("completed")
        self.longest_streak = quests.get("longest_streak")

    def repr(self):
        return f"DailyQuests(streak={self.streak}, completed={self.completed}, longest_streak={self.longest_streak})"
    
    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter((self.streak, self.completed, self.longest_streak))
