# sqlmap

**Service** | **Status**
------------ | -------------
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/14c98411d49b422f908fed0d02842cdb)](https://app.codacy.com/app/GermanAizek/sqlmap-python-3?utm_source=github.com&utm_medium=referral&utm_content=GermanAizek/sqlmap-python-3&utm_campaign=Badge_Grade_Dashboard)
**Azure:** | [![Build Status](https://dev.azure.com/GermanAizek/sqlmap3/_apis/build/status/GermanAizek.sqlmap-python-3?branchName=master)](https://dev.azure.com/GermanAizek/sqlmap3/_build/latest?definitionId=1&branchName=master)
**Travis CI:** | [![Build Status](https://api.travis-ci.org/sqlmapproject/sqlmap.svg?branch=master)](https://api.travis-ci.org/GermanAizek/sqlmap-python-3)

### Contacts

[![Python 3](https://img.shields.io/badge/python-3-yellow.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@sqlmap-blue.svg)](https://twitter.com/sqlmap)

Port by GermanAizek.

[![VK](https://img.shields.io/badge/VK-GermanAizek-blue.svg)](https://vk.com/germanaizek)
[![Facebook](https://img.shields.io/badge/Facebook-GermanAizek-blue.svg)](https://www.facebook.com/100024890867953)
[![Telegram](https://img.shields.io/badge/VK-GermanAizek-blue.svg)](https://t.me/germanaizek)

Original repositories: [![Original](https://img.shields.io/badge/GitHub-sqlmap-green.svg)](https://github.com/sqlmapproject/sqlmap)

sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

*The sqlmap project is sponsored by [Netsparker Web Application Security Scanner](https://www.netsparker.com/?utm_source=github.com&utm_medium=referral&utm_content=sqlmap+repo&utm_campaign=generic+advert).**

Screenshots
----

![Screenshot](https://raw.github.com/wiki/sqlmapproject/sqlmap/images/sqlmap_screenshot.png)

You can visit the [collection of screenshots](https://github.com/sqlmapproject/sqlmap/wiki/Screenshots) demonstrating some of features on the wiki.

Installation
----

You can download the latest tarball by clicking [here](https://github.com/sqlmapproject/sqlmap/tarball/master) or latest zipball by clicking  [here](https://github.com/sqlmapproject/sqlmap/zipball/master).

* Usage in Windows (if not python exists in ADD_PATH) or Ubuntu, MacOS

Preferably, you can download sqlmap by cloning the [Git](https://github.com/GermanAizek/sqlmap.git) repository:

    git clone https://github.com/GermanAizek/sqlmap-python-3.git
    cd sqlmap-python-3
    pip install -r requirements.txt
    
sqlmap works out of the box with [Python](http://www.python.org/download/) version **3.x** on any platform.

Usage
----

* Usage in any platform (Windows: if not python exists in ADD_PATH)

To get a list of basic options and switches use:

    python sqlmap.py -h

To get a list of all options and switches use:

    python sqlmap.py -hh
    
In Windows PowerShell:

    python .\sqlmap.py
    
*Caution do not confuse python3 or python

You can find a sample run [here](https://asciinema.org/a/46601).
To get an overview of sqlmap capabilities, list of supported features and description of all options and switches, along with examples, you are advised to consult the [user's manual](https://github.com/sqlmapproject/sqlmap/wiki/Usage).

Links
----

* Homepage: http://sqlmap.org
* Download: [.tar.gz](https://github.com/sqlmapproject/sqlmap/tarball/master) or [.zip](https://github.com/sqlmapproject/sqlmap/zipball/master)
* Commits RSS feed: https://github.com/sqlmapproject/sqlmap/commits/master.atom
* Issue tracker: https://github.com/sqlmapproject/sqlmap/issues
* User's manual: https://github.com/sqlmapproject/sqlmap/wiki
* Frequently Asked Questions (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
* Twitter: [@sqlmap](https://twitter.com/sqlmap)
* Demos: [http://www.youtube.com/user/inquisb/videos](http://www.youtube.com/user/inquisb/videos)
* Screenshots: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots

Translations
----

* [Bulgarian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-bg-BG.md)
* [Chinese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-zh-CN.md)
* [Croatian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-hr-HR.md)
* [French](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-fr-FR.md)
* [Greek](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-gr-GR.md)
* [Indonesian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-id-ID.md)
* [Italian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-it-IT.md)
* [Japanese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ja-JP.md)
* [Polish](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pl-PL.md)
* [Portuguese](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md)
* [Russian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-ru-RUS.md)
* [Spanish](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-es-MX.md)
* [Turkish](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-tr-TR.md)
* [Ukrainian](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-uk-UA.md)
