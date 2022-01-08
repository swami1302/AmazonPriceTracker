import requests
from bs4 import BeautifulSoup
import smtplib
import time


print("hello world")
desired_price=int(input("enter the desired amount: "))
parsing_time=int(input("enter time gap between your search"))

url="https://www.amazon.in/MJSXJ02CM-1080P-Security-Camera-White/dp/B07HJD1KH4/ref=sr_1_3?dchild=1&keywords=camera&qid=1633578421&sr=8-3" #get from user

header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"} 


def check_price():
    page=requests.get(url, headers=header) #returns all the data from the website

    soup=BeautifulSoup(page.content,'html.parser') #used to pull out individual items

    #print(soup.prettify()) 

    title=soup.find(id="productTitle").getText()

    print(title.strip()) #to remover extra space

    try:
        price=soup.find(id="priceblock_dealprice").getText()
    except:
        price=soup.find(id="priceblock_ourprice").getText()

    if len(price)<=7:
        converted_price=price[1:7].replace(",","")
        converted_price=float(converted_price)
    else:
        converted_price=price[1:10].replace(",","")
        converted_price=float(converted_price)

    print(converted_price)

    if converted_price<=desired_price:
        send_mail()
    else:
        print("Sorry the price hasn't been fell down check later")

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #establish connection between serever and mail
    server.starttls() #encrypts the connection
    server.ehlo() 
    server.login('technolov123@gmail.com','vsbnatrnjskzptip') #temp password

    subject="price fell down!!" 
    body=("check the price once again with link below ",url)
    msg=f'Subject:{subject}\n\n{body}' 

    server.sendmail( 

        'technolov123@gmail.com', #from
        'swaminathan13022003@gmail.com', #to
        msg #message

    ) 

    print('\n e-mail has been sent') 

    server.quit()

while True:
        check_price()
        time.sleep(parsing_time)