from tkinter import *
from tkinter import messagebox, Tk
import smtplib
import math, random
from logging import root
import time, os, sys
import pyautogui
import keyboard
from bs4 import BeautifulSoup
import requests
import time
import re
from threading import Thread
from email.mime.text import MIMEText as text


root:Tk = Tk(screenName=None, baseName=None, className=' Product Price Tracker', useTk=1)
header = Label(root, text="PRODUCT PRICE TRACKER", bg='#ffff99', fg='#2db300', font='Monotype_Corsiva 28 bold', pady=15)
header.pack()

root.configure(bg='#ffff99')
frame1 = Frame()
frame1.pack()


def options():
    L3.forget()
    B1.forget()
    enter_otp_entry.forget()
    B2.forget()
    global Flipkart_Button
    Flipkart_Button = Button(root, text='Flipkart', width=70, height=5, activebackground='white', bg='yellow',
                             fg='blue', font='Helvetica 12 bold', command=frm2)
    Flipkart_Button.pack(side=TOP, padx=10, pady=10)
    global Myntra_Button
    Myntra_Button = Button(root, text='Reliance Digital', width=70, height=5, activebackground='white', bg='pink',
                           fg='red', font='Helvetica 12 bold', command=frm3)
    Myntra_Button.pack(side=TOP, padx=15, pady=15)
    restart_Button = Button(root, text='Restart', width=30, activebackground='white', bg='red', command=restart)
    restart_Button.pack(side=BOTTOM)


def frm2():
    L3.forget()
    B1.forget()
    enter_otp_entry.forget()
    B2.forget()
    # next2_button.forget()

    Flipkart_Button.forget()
    Myntra_Button.forget()
    # restart_Button.forget()
    global amazon_URL_Label
    amazon_URL_Label = Label(root, text='Enter Flipkart product page link:', bg='yellow', fg='blue')
    amazon_URL_Label.pack(side=TOP, padx=5, pady=5)
    global amazon_URL
    amazon_URL = Entry(root, width=50)
    amazon_URL.pack(side=TOP, padx=5, pady=5)
    global amazon_sel_price_label
    amazon_sel_price_label = Label(root, text='Enter a trigger price :', bg='yellow', fg='blue')
    amazon_sel_price_label.pack(side=TOP, padx=5, pady=5)
    global amazon_sel_price
    amazon_sel_price = (Entry(root, width=5))
    amazon_sel_price.pack()
    global amazon_time_label
    amazon_time_label = Label(root, text='Select the time interval to check the price:', bg='yellow', fg='blue')
    amazon_time_label.pack(side=TOP, padx=5, pady=5)
    global amazon_time
    amazon_time = Listbox(root, bg='yellow', fg='blue')
    amazon_time.insert(0, '30 seconds')
    amazon_time.insert(1, '1 minute')
    amazon_time.insert(2, '10 minute')
    amazon_time.insert(3, '30 minutes')
    amazon_time.insert(4, '1 hour')
    amazon_time.insert(5, '12 hour')
    amazon_time.insert(6, '1 day')
    amazon_time.pack()
    # submit button - add command to button later:
    global walmart_Submit_Button
    walmart_Submit_Button = Button(root, text='Submit', width=30, activebackground='white', bg='#e6e600', fg='blue',
                                   command=submit_button1)
    walmart_Submit_Button.pack()
    # restart_Button.pack(side = BOTTOM)


def frm3():
    L3.forget()
    B1.forget()
    enter_otp_entry.forget()
    B2.forget()
    # next2_button.forget()

    Flipkart_Button.forget()
    Myntra_Button.forget()
    # restart_Button.forget()
    global amazon_URL_Label
    amazon_URL_Label = Label(root, text='Enter Reliance Digital product page link:', bg='pink', fg='red')
    amazon_URL_Label.pack(side=TOP, padx=5, pady=5)
    global amazon_URL
    amazon_URL = Entry(root, width=50)
    amazon_URL.pack(side=TOP, padx=5, pady=5)
    global amazon_sel_price_label
    amazon_sel_price_label = Label(root, text='Enter a trigger price :', bg='pink', fg='red')
    amazon_sel_price_label.pack(side=TOP, padx=5, pady=5)
    global amazon_sel_price
    amazon_sel_price = (Entry(root, width=5))
    amazon_sel_price.pack()
    global amazon_time_label
    amazon_time_label = Label(root, text='Select the time interval to check the price:', bg='pink', fg='red')
    amazon_time_label.pack(side=TOP, padx=5, pady=5)
    global amazon_time
    amazon_time = Listbox(root, bg='pink', fg='red')
    amazon_time.insert(0, '30 seconds')
    amazon_time.insert(1, '1 minute')
    amazon_time.insert(2, '10 minute')
    amazon_time.insert(3, '30 minutes')
    amazon_time.insert(4, '1 hour')
    amazon_time.insert(5, '12 hour')
    amazon_time.insert(6, '1 day')
    amazon_time.pack()
    # submit button - add command to button later:
    global walmart_Submit_Button
    walmart_Submit_Button = Button(root, text='Submit', width=30, activebackground='white', bg='#99004d',
                                   command=submit_button2)
    walmart_Submit_Button.pack()
    # restart_Button.pack(side = BOTTOM )


def flipkart_link_verification(f):
    x = f[12:20]
    b = "flipkart"

    if x == b:
        return True
    else:
        return False


def flipkart_details(url):
    cont = requests.get(url)
    htmlcontent = cont.content

    soup = BeautifulSoup(htmlcontent, "html.parser")

    # name of product
    try:
        title = soup.find("span", class_="B_NuCI").text
        title = title.split(")")[0] + ")"
        # print(title)
    except:
        title = "n/a"

    # price of product
    try:
        price = soup.find("div", class_="_30jeq3 _16Jk6d").text
        price = price.replace("₹", "")
        price = price.replace(",", "")
        price = int(price)
        # print(price)
    except:
        price = 'n/a'

    # reviews of product
    try:
        total_rating = soup.find("span", class_="_2_R_DZ").text
        review = total_rating.split()[3].replace(",", "")
        # print(review)
    except:
        review = "n/a"

    # total ratings of product
    try:
        total_rating = soup.find("span", class_="_2_R_DZ").text
        total_rating = total_rating.split()[0].replace(",", "")
        # print(total_rating)
    except:
        total_rating = 'n/a'

    # rating of product
    try:
        rating = soup.find("div", class_="_3LWZlK").text
        # print(rating)
    except:
        rating = "n/a"

    return [title, price, total_rating, review, rating]


def compare1(link1, interval1, target1):
    while (1):
        try:
            current = flipkart_details(link1)
            if (current[1] <= int(target1)):
                send_update_flipkart(link1)
                messagebox.showinfo("Congrats", "MRP under budget !! An Email has been sent successfully.")
            #    m_duration_1 = 5000
            #    m_1 = 'MRP below target'
            #    top = Toplevel()
            #    top.title()
            #    Message(top, text=m_1, padx=25, pady=20).pack()
            #    top.after(m_duration_1, top.destroy)

                print(0)
                break
            else:
                messagebox.showinfo("Checking", "MRP above budget.")
            #    m_duration_2 = 8000
            #    m_2 = 'MRP below target'
            #    top = Toplevel()
            #    top.title()
            #    Message(top, text=m_1, padx=25, pady=20).pack()
            #    top.after(m_duration_1, top.destroy)
                print(1)
        except:
            messagebox.showinfo("Error", "Server error. Try again after some time.")
            break
        time.sleep(interval1)


def submit_button1():

    link1 = target1 = interval1 = ""

    link1 = amazon_URL.get()
    target1 = amazon_sel_price.get()
    interval1 = amazon_time.curselection()

    if (link1 == "" or interval1 == "" or target1 == "") and (flipkart_link_verification(link1)):
        messagebox.showinfo("Error", "Please fill all fields!")

    else:
        print(interval1)
        if (interval1[0] == 0):
            interval1 = 30
        elif (int(interval1[0]) == 1):
            interval1 = 60
        elif (int(interval1[0]) == 2):
            interval1 = 600
        elif (int(interval1[0]) == 3):
            interval1 = 180
        elif (int(interval1[0]) == 4):
            interval1 = 3600
        elif (int(interval1[0]) == 5):
            interval1 = 12 * 60 * 60
        else:
            interval1 = 24 * 60 * 60

        new_thread1 = Thread(target=compare1(link1, interval1, target1))
        new_thread1.start()


def reliance_digital(url):
    cont = requests.get(url)
    html = cont.content
    soup = BeautifulSoup(html, "html.parser")

    # name of product
    try:
        title = soup.find("h1", class_="pdp_title mb_20").text
    except:
        title = "n/a"

    # offer price of product
    try:
        price = soup.find("span", class_="pdp__offerPrice").text
        price = price.replace("₹", "")
        price = price.replace(",", "")
        price = int(float(price))
    except:
        price = 'n/a'

    # MRP of product
    try:
        MRP = soup.find("span", class_="pdp__MRPPrice").text
        MRP = MRP.replace("₹", "")
        MRP = MRP.replace(",", "")
    except:
        MRP = 'n/a'

    # current savings of product
    try:
        offer = soup.find("li", class_="pdp_priceSectionpriceListText pdp_savePrice").text
        offer = offer.split(" ")
        offer = offer[2]
        offer = offer.replace(",", "")
        offer = offer.replace("₹", "")
    except:
        offer = 'n/a'

    # #image
    # try:
    #     #abcd = soup.findAll("img")
    #     #print(abcd[7].attrs['src'])
    #     ab = soup.find("rect",calss = "highcharts-background")
    #     print(ab)

    # except:
    #     pass

    return [title, price, MRP, offer]


def compare2(link2, interval2, target2):
    while (1):
        try:
            current = reliance_digital(link2)
            if (current[1] <= int(target2)):
                messagebox.showinfo("Congrats", "MRP under budget !! An Email has been sent successfully.")
                send_update_reliance(link2)
            #    m_duration_1 = 5000
            #    m_1 = 'MRP below target'
            #    top = Toplevel()
            #    top.title()
            #    Message(top, text=m_1, padx=25, pady=20).pack()
            #    top.after(m_duration_1, top.destroy)
                print(0)
                break
            else:
                messagebox.showinfo("Checking", "MRP above budget.")
                #    m_duration_1 = 5000
                #    m_1 = 'MRP below target'
                #    top = Toplevel()
                #    top.title()
                #    Message(top, text=m_1, padx=25, pady=20).pack()
                #    top.after(m_duration_1, top.destroy)

                print(1)

        except:
            messagebox.showinfo("Error", "Server error. Try again after some time.")
            break
        time.sleep(interval2)


def submit_button2():
    link2 = amazon_URL.get()
    target2 = amazon_sel_price.get()
    interval2 = amazon_time.curselection()
    print(link2, target2, interval2)

    if link2 == "" or interval2 == "" or target2 == "":
        messagebox.showinfo("Error", "Please fill all fields!")
    else:
        if (interval2[0] == 0):
            interval2 = 30
        elif (int(interval2[0]) == 1):
            interval2 = 60
        elif (int(interval2[0]) == 2):
            interval2 = 600
        elif (int(interval2[0]) == 3):
            interval2 = 180
        elif (int(interval2[0]) == 4):
            interval2 = 3600
        elif (int(interval2[0]) == 5):
            interval2 = 12 * 60 * 60
        else:
            interval2 = 24 * 60 * 60
        new_thread2 = Thread(target=compare2(link2, interval2, target2))
        new_thread2.start()




def stop(event):
    keyboard.on_press_key("Esc", stop)


def stop(event):
    global running
    running = False
    root.bind("<Escape>", stop)

def restart():
    # os.execv(sys.executable, [sys.executable] + sys.argv)
    os.execv(sys.executable, [sys.executable, '"' + sys.argv[0] + '"'] + sys.argv[1:])


email_label = Label(root, text="Enter receiver's Email: ", font=("ariel 15 bold"), relief=FLAT)
email_label.pack(side=TOP)
email_entry = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
email_entry.pack(side=TOP)
email_entry.focus()


def send_update_flipkart(link1):
    username = '2020.sparsh.verma@ves.ac.in'
    password = 'SpartanKing@0210'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    m = text("Product Link: " + link1 + "\n" + "Heyy !!! Congrats your product price has reached to your budget, you can now buy your product :)")
    m['From'] = '2020.sparsh.verma@ves.ac.in'
    m['To'] = email_entry.get()
    m['Subject'] = 'PRICE DROP'
    server.sendmail("2020.sparsh.verma@ves.ac.in", email_entry.get(), m.as_string())
    server.quit()

def send_update_reliance(link2):
    username = '2020.sparsh.verma@ves.ac.in'
    password = 'SpartanKing@0210'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    m = text("Product Link: " + link2 + "\n" + "Heyy !!! Congrats your product price has reached to your budget, you can now buy your product :)")
    m['From'] = '2020.sparsh.verma@ves.ac.in'
    m['To'] = email_entry.get()
    m['Subject'] = 'PRICE DROP'
    server.sendmail("2020.sparsh.verma@ves.ac.in", email_entry.get(), m.as_string())
    server.quit()


global OTP
OTP = ""
resend_OTP = ""
digits = "0123456789"
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
    resend_OTP += digits[math.floor(random.random() * 10)]

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def sendemail():
    if (re.fullmatch(regex, email_entry.get())):

        username = '2020.sparsh.verma@ves.ac.in'
        password = 'SpartanKing@0210'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        m = text("Hello your otp is " + OTP)
        m['From'] = '2020.sparsh.verma@ves.ac.in'
        m['To'] = email_entry.get()
        m['Subject'] = 'Email Verification for PRICE DROP'
        server.sendmail("2020.sparsh.verma@ves.ac.in", email_entry.get(), m.as_string())
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")
        server.quit()
        otp()

    else:
        messagebox.showinfo("Error", "Please Enter A Valid Email ID")


# get_otp: str = enter_otp_entry.get()

def otp():
    def resendemail():


            username = '2020.sparsh.verma@ves.ac.in'
            password = 'SpartanKing@0210'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            m = text("Hello your otp is " + resend_OTP)
            m['From'] = '2020.sparsh.verma@ves.ac.in'
            m['To'] = email_entry.get()
            m['Subject'] = 'Email Verification for PRICE DROP'
            server.sendmail("2020.sparsh.verma@ves.ac.in", email_entry.get(), m.as_string())
            messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")
            server.quit()



    email_label.forget()
    email_entry.forget()
    send_button.forget()
  # next1_button.forget()

    global L3
    L3 = Label(root, text="Enter OTP", font=(None, 25), bg="navyblue", fg="white", padx=100)
    L3.pack()
    global B1
    B1 = Button(root, text="Resend OTP", command=resendemail, bg="#6f6")
    B1.pack()

    global enter_otp_entry
    enter_otp_entry = Entry(root)
    enter_otp_entry.pack()
    enter_otp_entry.insert(0, "")

    global B2
    B2 = Button(root, text="  Submit  ", bg="#6f6", command=otp_verfication)
    B2.pack()


#   next2_button = Button(root, text='Next', font=("ariel 15 bold"), bg="black", fg="green2", bd=3, command=options)
#   next2_button.pack(side=TOP)

def otp_verfication():
    global OTP
    if (enter_otp_entry.get() == OTP):
        options()
        OTP = ""
    elif (enter_otp_entry.get() == resend_OTP):
        options()
    else:
        messagebox.showinfo("Error", "Please Enter Correct OTP")



def email_verificaition(email):
    if (re.search(regex, email)):
        otp()

    else:
        messagebox.showinfo("Error", "Please Enter A Valid Email ID")


send_button = Button(root, text="Send OTP", font=("ariel 15 bold"), bg="black", fg="green2", bd=3, command=sendemail)
send_button.pack(side=TOP)
# next1_button = Button(root, text = 'Next', font = ("ariel 15 bold"), bg="black", fg="green2", bd=5, command=otp )
# next1_button.pack(side= LEFT)


root.mainloop()
