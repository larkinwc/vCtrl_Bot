.. vCtrl Discord Bot documentation master file, created by
   sphinx-quickstart on Fri May 11 20:02:05 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to vCtrl Discord Bot's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Features
--------

- Automaticall capture binary files that are shared via discord
- Annoy you if you send too many attachments! 

Commands
--------

$status - Gives you info on the currently setup repo 
$undo - Undoes the last commit 
$ignore - This will ignore the specified . extension from being added to version control.
$pull - this will pull any commits from the GitHub repo
$help - this will say you can use commands to view commands, and also link the documentation page for this bot.
$commands - lists usable commands

Installation
------------

Prereqs
------------
Python 3.5+
Discord.py 0.16+
PyGithub 1.3x+
GitPython 2.1.9+
aiohttp 1.0.5+
urllib3 1.22+


Run vCtrl by running:

    python3 main.py

=============================
API Reference

Classes:

Version - contains main git commands and tracks how many commits have been made 
    setup(repoName):
        """ this should be run if a repo hasn't been initialized yet. """

    do_commit(files):
        """ using path file, add file to project if not already included, otherwise update it """
    
    undo_commit(commit = 0):
        """ given a commit (defaults to last commit id), undo it """

    get_commitID():
        """ returns last commit performed """

    get_info():
        """ will use github package to find out the current status of the repo, total commits and time last updated """

    write_settings():
        """ writes settings to settings.txt so in future sessions the info will not need to be input again. """
      



Contribute
----------

- Issue Tracker: https://github.com/luhrkin/vCtrl_bot/issues
- Source Code: https://github.com/luhrkin/vCtrl_bot

Support
-------

If you are having issues, please let me know.
email me at larkinwc@utexas.edu

License
-------

The project is licensed under the MIT license.