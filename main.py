import nitendo_selenium
import os
os.environ['USER_ID'] = 'U905070f20dd358b401940636b6c8372e'
os.environ['YOUR_CHANNEL_ACCESS_TOKEN'] = 'URQLboUaLDkxgAhcuacRX01xVhibclbFBg9U42zWOpEHEki9AQ9CGMTLsSWq2N1quMi+U8dCNf+9OIoPkInM7lo9yM8K2fgccaqFjyFn+p5ia2I4bc/NPQ26lWPBN6D7iPX83RAogX3/RMmjl6DIDwdB04t89/1O/w1cDnyilFU='
os.environ['YOUR_CHANNEL_SECRET'] = '49a12cdf75313693d449116966e12838'
import linebot_tutorial

if nitendo_selenium.main() is True:
    linebot_tutorial.push_mes()
else:
    print('特に動きなし')