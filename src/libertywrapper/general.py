import datetime

from .activity import UserActivity, UserQuestsActivity, UserJobsActivity
from .base.general import ServerOnlineHistory

class General:
    def __init__(self, data, **kwargs):
        self.total_users = data.get("total_users")
        self.total_online = data.get("total_online")
        self.total_vehicles = data.get("total_vehicles")
        self.total_houses = data.get("total_houses")
        self.total_apartments = data.get("total_apartments")
        self.total_posts = data.get("total_posts")

        self.top_users_activity = [UserActivity(**x) for x in data.get("top_users_activity")]
        self.top_users_last_week_activity = [UserQuestsActivity(**x) for x in data.get("top_users_last_week_activity")]
        self.top_users_quests = [UserQuestsActivity(**x) for x in data.get("top_users_quests")]
        self.top_users_jobs = [UserJobsActivity(**x) for x in data.get("top_users_jobs")]
        
        self.online_history = [ServerOnlineHistory(x) for x in data.get("online_history")]

    def repr(self):
        return f"General(total_users={self.total_users}, total_online={self.total_online}, total_vehicles={self.total_vehicles}, total_houses={self.total_houses}, total_apartments={self.total_apartments}, total_posts={self.total_posts}, top_users_activity={self.top_users_activity}, top_users_last_week_activity={self.top_users_last_week_activity}, top_users_quests={self.top_users_quests}, top_users_jobs={self.top_users_jobs}, online_history={self.online_history})"

    def __repr__(self):
        return self.repr()

    def __iter__(self):
        return iter(self.__dict__.items())
    