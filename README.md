
# LibertyWrapper

Unofficial Python API Wrapper for the [Liberty.MP](https://ucp.liberty.mp/) RageMP Server.


## Installing

You can install it via pip using: <br>
`pip install libertywrapper`

## Usage

In order to fetch data, a `Wrapper` object is required.
```py
import libertywrapper.bot
wrapper = libertywrapper.bot.Wrapper()
```
Optionally, you can specify an username and password (a set of credentials from the [liberty.mp UCP](https://ucp.liberty.mp/)) in order to get private data like a player's statistics. <br>
```py
wrapper = libertywrapper.bot.Wrapper(username='username', password='password')
```

### Methods

The `Wrapper` object does have the following methods:

|Method name     |Return                          |Requires credentials|
|----------------|-------------------------------|-----------------------------|
|fetch_homepage()            |General() object|❌|
|fetch_staff()          |Staff() object|❌|
|fetch_online_players()          |List of BriefUser() objects|❌|
|fetch_map_blips()          |List of MapBlip() objects|❌|
|search_user(nickname)          |List of UserSearchResult() objects|❌|
|fetch_factions()          |List of Faction() objects|❌|
|fetch_user(nickname)          |Player() object|✔|

### Example

```py
 homepage = wrapper.fetch_homepage()
 
 online_players = homepage.total_online
 posts_number = homepage.total_posts
 print(online_players, posts_number) # integers

 for user in homepage.top_users_activity:
	 print(user.name, user.level, self.avatar) # "username", 10, https://imgur.com/example
	 print(user.playtime) # 10:23:00 (datetime.timedelta object)
```

##  Updates
  
  Complete documentation is going to be added on the future releases.
