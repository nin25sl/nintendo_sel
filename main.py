import nitendo_selenium
import os
import linebot_tutorial

if nitendo_selenium.main() is True:
    linebot_tutorial.push_mes()
else:
    print('特に動きなし')