# General Info
This is a Discord bot written in Python that allows you to create Trello tickets from discord messages. It uses the discordpy library and the py-trello library.
This requires a basic understanding of both Discord Bots and the Trello API.

# Dependencies

```bash

pip install discord.py
pip install py-trello

```

# Setup
1. Clone the repository.
2. Open main.py and add your Discord Bots Token in line 10.
3. Open trelloAPI.py and add your Trello api_key,api_secret and token in line 7,8 and 9
4. In trelloAPI.py edit board="NAME_OF_YOUR_TRELLO_BOARD" to your actual Trello Board name and edit trelloList="NAME_OF_YOUR_TRELLO_LIST" to the name of the list in which you want o the bugs to go.

# References
[Trello API Info](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)
[Discord.py Info](https://discordpy.readthedocs.io/en/stable/intro.html)
[Create a Discorb Bot](https://discord.com/developers/docs/getting-started)
