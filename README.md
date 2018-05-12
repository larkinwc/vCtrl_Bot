[![Documentation Status](https://readthedocs.org/projects/vctrl-bot/badge/?version=latest)](http://vctrl-bot.readthedocs.io/en/latest/?badge=latest)


# vCtrl_Bot

vCtrl is a chat bot, whose goal is to assimilate all the binary files that are shared in your chat into a repo. In the future this bot will support Slack, Unity builds, and SVN, so we can achieve our goal to help integrate as many chat platforms as possible. 

## Getting Started

Currently the installation process for this bot is self hosted, as Heroku support is forthcoming once the bot can accept invites to servers, and differentiate the respective server's repos. 

### Prerequisites


```
Python 3.5+
Discord.py 0.16+
PyGithub 1.3x+
GitPython 2.1.9+
aiohttp 1.0.5+
urllib3 1.22+
```

### Installing

Simple self hosted install - auto

```
1. Create a discord app at https://discordapp.com/developers/applications/me/create , 
   and input your bot's token on line #18
2. Create a repo on your Github account, and get an oAuth key for said Github account
3. Install all Prequisites
4. Run main.py
5. Input information when promted
```

Alternate Installation

```
1. Create a discord app at https://discordapp.com/developers/applications/me/create , 
   and input your bot's token on line #18
2. Create a repo on your Github account, and get an oAuth key for said Github account
3. Install all Prequisites
4. Edit line #12 with your Github key
5. Input information when promted
```

Test the bot by sending a binary file in your chat.


## Deployment

Eventually this bot will be available to invite to your server, so you do not have to host your own instance.

## Built With

* [Discord.py](https://github.com/Rapptz/discord.py) - The discord API wrapper that was used
* [GitPython](https://github.com/gitpython-developers/GitPython) - Git wrapper to be implemented
* [PyGithub](https://github.com/PyGithub/PyGithub) - Used to grab and upload files to repos

## Contributing

TBA

## Versioning

This project is currently in pre-alpha, v0.001a. 

Versioning 

## Authors

* **Larkin Williams-Capone** - *Main Developer* - [Personal Site](http://larkinwc.com/) and [Github](https://github.com/luhrkin)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Professor Michael Baker of the University of Texas at Austin
* I would also like to thank the School of Design and Creative Technologies at UT for the amazing academic program that is being developed here.


# One small version control bot, one large step at a time.
