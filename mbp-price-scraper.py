#importing libraries
from bs4 import BeautifulSoup
#import re
import urllib.request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = "https://www.flipkart.com/apple-macbook-pro-core-i5-8th-gen-8-gb-128-gb-ssd-mac-os-mojave-muhn2hn-a/p/itmfgpwanmhejpaf?pid=COMFGPWAGXNPSTY2&srno=s_1_7&otracker=search&otracker1=search&lid=LSTCOMFGPWAGXNPSTY2KWEZOW&fm=SEARCH&iid=440ca833-39a7-4712-b142-392c5e6c15ac.COMFGPWAGXNPSTY2.SEARCH&ppt=sp&ppn=sp&ssid=uwbp1vw7yo0000001572702453313&qH=0dcf1970a1af488e"
try:
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    price = soup.find("div", attrs={'class': '_3qQ9m1'}).getText()
except:
    print("An error occured.")
   
#removing ₹ and ',' from the price
price = price[1:].replace(',', '')

#reading from the file
f = open("price_file.txt", "r")
old_price = f.read()

if int(price) < int(old_price):
#if True:
    #writing the price to the file
    f = open("price_file.txt", "w+")
    f.write(price)
    f.close()

    #setting the smtp server
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login("pearelexps@gmail.com", "thisisn0tthepa$sw0rd")

    #message to be sent
    message = "The price of the Macbook Pro just dropped to " + price
    msg = MIMEMultipart()
    msg['From'] = "pearelexps@gmail.com"
    msg['To'] = "pearel@outlook.com"
    msg['Subject'] = "Price drop for MBP"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)

    del(msg)