# Callie
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Star this repository](https://img.shields.io/github/stars/kevinam99/Callie?style=social)



Callie is simply a web implementattion of [this](https://github.com/kevinam99/Instagram-Like-Bot) project created by me a few months ago. I thought of making a web version of this so it is easy to show it to anyone, anywhere.

The [`master`](https://github.com/kevinam99/Callie/) branch contains development from localhost and everything works perfectly. The production version is in the [`heroku`](https://github.com/kevinam99/Callie/tree/heroku) branch. Callie has been deployed [here on Heroku](https://callie-kevinam99.herokuapp.com/).

There are a lot of problems while running the app on Heroku. I tried umpteen Firefox and Geckodriver buildpacks but nothing worked. So I decided to use the Chrome webdriver, but still there are issues creeping up.

The `master` uses Firefox webdriver and `heroku` uses Chrome webdriver from ``` Selenium ```. 



## Usage:
1. Start a Python virtual environment (Preferably using pipenv)
2. Install the packages using the command ```pipenv install```.
3. Once the packages are installed start the bot by entering either ```flask run``` or ```gunicorn run:app```.

## Stack
- Python 3.6
- Flask 1.12

### Reach out to me on:
1. [Twitter](https://www.twitter.com/kevin_codes)
2. [Instagram](https://www.instagram.com/kevin.codes)
3. Email <kevinam99@gmail.com>
4. [LinkedIn](https://www.linkedin.com/in/kevin-a-mathew)

Check out this nifty little script, [Reuben](https://github.com/kevinam99/Reuben), which helps in quickly setting up a Flask project.