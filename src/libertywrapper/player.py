import datetime

from .base.game import Item, Inventory, AchievementProgress, Comment, Vehicle, PanelSettings, Character, BusinessShare
from .base.staff import StaffPerms
from .base.data import Log
from .base.general import JobEarnings

class Player:
    def __init__(self, data) -> None:
        self.panel_settings = PanelSettings(data.get("PanelSettings"))
        if self.panel_settings.private_profile:
            raise Exception("Profile is private!")
            # https://cdn2.hubspot.net/hubfs/3350762/Cheetoh%20in%20Lock.jpg
            
        self.id = data.get("id")
        self.name = data.get("name")
        self.avatar = data.get("UserAvatar")
        self.level = data.get("Level")
        self.phone_number = data.get("PhoneNumber")
        self.status = data.get("Status")

        self.playtime = datetime.timedelta(seconds=data.get("Playtime"))
        # "2023-04-10T15:13:20.064Z"
        self.created_at = datetime.datetime.fromisoformat(data.get("createdAt").replace("Z", "+00:00"))
        self.last_online = datetime.datetime.fromisoformat(data.get("lastOnline").replace("Z", "+00:00"))
        
        self.character = Character(**data.get("Character"))
        self.perms = StaffPerms(data.get("sPermissions"))
        #  self.faction = FactionUser(id=data.get("Faction"), rank=data.get("FactionRank"), name=data.get("faction").get("Name")) if data.get("Faction") else None
        
        self.premium_type = data.get("Premium").get("type")
        self.premium_expiration = datetime.timedelta(seconds=data.get("Premium").get("expirationDate"))

        self.web_suspend = data.get("WebSuspend")
        self.job_earnings = JobEarnings(**data.get("JobEarnings"))
        
        self.inventory = Inventory(data.get("Inventory"))
        self.post_office_items = [Item(item) for item in data.get("PostOfficeItems")]

        self.personal_vehicles = [Vehicle(vehicle) for vehicle in data.get("personal_vehicles")]
        
        self.profile_comments = [Comment(comment) for comment in data.get("profile_comments")]

        self.achievements = [AchievementProgress(achievement) for achievement in data.get("achievement_progresses")]

        self.ban = data.get("ban")
        self.faction_history = [Log(log) for log in data.get("faction_logs")]

        self.business_shares = [BusinessShare(share) for share in data.get("biz_shares")]
        self.admin_label = data.get("AdminLabel") # Neimplementat in UCP
        self.following = data.get("following") # Neimplementat in UCP
        self.followers = data.get("followers") # Neimplementat in UCP

    def repr(self) -> str:
        return f"<Player {self.name} | {self.id}>"
    
    def __str__(self) -> str:
        return self.repr()
    
    def __repr__(self) -> str:
        return self.repr()
    
