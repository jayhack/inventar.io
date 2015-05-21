# Inventar.io
A platform for building connectivity apps through email and SMS

## I. Overview

Inventar.io is a platform that allows developers to rapidly develop and deploy web applications that interact with their users through email and SMS. This is particularly handy in areas where internet access relatively hard to come by (Cuba) but there is widespread and affordable access to email and/or SMS. Example applications include:

  - wiki: email wiki@ivioapp.com with a concept in thes subject line to receive a wikipedia summary
  
  - clima: email clima@ivioapp.com to receive the current weather in Havana

Inventar.io provides developers with simple access to SMS and email messaging services as well as NoSQL database storage. This allows one to emulate a huge range of popular web services for those without affordable access. Please help us scale horizontally - make craigslist/twitter/yikyak/whatever accessible via email! - and provide valuable services to those in need.


## II. Setup

	~$: git clone https://www.github.com/jayhack/inventar.io.git


## III. Contributing to the Project

Developers can contribute to the project by following these steps:

  1. Clone the repo

  2. Create a new subclass of inventario.EmailBaseApp or inventario.SMSBaseApp in a file with your app's name, implementing your app's logic. See `inventario/apps/helloworld.py` for a tutorial on how to do so.

  3. Make a pull request and/or email me at jhack@stanford.edu.

Thanks!


## IV. App Wish List

The following apps would be amazing:

  - cultura@ivioapp.com: scrape common Cuban websites to find public cultural gatherings, then offer them up in a digest for anyone who emails this endpoint.

  - craigslist@ivioapp.com: allow people to email in items they have and/or items they want, then connect buyers and sellers if there is a match

  - rideshare@ivioapp.com: allow people to share when and where they will be embarking upon a road trip, along with how many seats they have available, in order to match people for rides


## Contact:

Comments/questions? Ideas? Issues you have noticed? Feel free to hit me up!

  Jay Hack

  github.com/jayhack

  jhack@stanford.edu

