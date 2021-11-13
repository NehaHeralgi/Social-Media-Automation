import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image
from instabot import Bot
import os
import glob

global driver
#cookie_del = glob.glob("config/*cookie.json")
#os.remove(cookie_del[0])

w1=Tk()
w1.title('Social Media Automation!')
w1width = 1000
w1height = 600
x = int((w1.winfo_screenwidth()/2) - (w1width/2))
y = int((w1.winfo_screenheight()/2) - (w1height/2))
w1.geometry(f"+{x}+{y}")

c1 = Canvas(w1, width = 1000, height = 600)      
c1.pack()

bg = ImageTk.PhotoImage(Image.open('C:/Users/Neha/Downloads/mini_2A/mini_2A/background.jpg'))
c1.create_image(0, 0, image=bg, anchor='nw')

c1.create_text(245,50,text='Social Media Automation',font="Calibri 30", fill='#00FFFF', anchor='nw')
c1.create_text(425,110,text='Group 09',font="Calibri 20", fill='#00FF00', anchor='nw')

c1.create_text(145,220,text='Need a break from social media posting? Try automating your posts by',font='Arial 14', fill='yellow', anchor='nw')
c1.create_text(325,250,text='pressing the buttons below to start!',font='Arial 14', fill='yellow', anchor='nw')

def instagram():
    w1.withdraw()
    w2=Toplevel()
    
    w2.title('Automate Your Instagram!')
    w2width = 1000
    w2height = 600
    x = int((w2.winfo_screenwidth()/2) - (w2width/2))
    y = int((w2.winfo_screenheight()/2) - (w2height/2))
    w2.geometry(f"+{x}+{y}")

    c2 = Canvas(w2, width = 1000, height = 600)      
    c2.pack()

    bg = ImageTk.PhotoImage(Image.open('C:/Users/Neha/Downloads/mini_2A/mini_2A/instagram.jpg'))
    c2.create_image(0, 0, image=bg, anchor='nw')

    c2.create_text(330,20,text='Enter your details to login',font='Verdana 16', fill='white', anchor='nw')

    c2.create_text(340,80,text='Username:',font='Verdana 12', fill='white', anchor='nw')
    t1=Entry(c2,width=15,font='Verdana 12',bg='white',fg='black')
    t1.place(x=470,y=80)

    c2.create_text(340,120,text='Password:',font='Verdana 12', fill='white', anchor='nw')
    t2=Entry(c2,show="*",width=15,font='Verdana 12',bg='white',fg='black')
    t2.place(x=470,y=120)

    def login():
        bot=Bot()
        bot.login(username=t1.get(), password=t2.get())
        loggedin=True

        if loggedin:
            c2.create_text(80,280,text='Upload a Post',font='Verdana 14', fill='white', anchor='nw')
            c2.create_text(15,330,text='Caption:',font='Verdana 12', fill='white', anchor='nw')
            t3=Entry(c2,width=12,font='Verdana 12',bg='white',fg='black')
            t3.place(x=105,y=330)

            def fileDialog():
                path = filedialog.askopenfilename()
                bot.upload_photo(path, caption=t3.get())

            Button(c2, text="Choose image & post",font=('Comic Sans MS', 10), width=16, height=1, bg='#00FF00', fg='black', command=fileDialog).place(x=70,y=370)

            c2.create_text(380,280,text='Like & Unlike Post',font='Verdana 14', fill='white', anchor='nw')
            c2.create_text(350,330,text='Username:',font='Verdana 12', fill='white', anchor='nw')
            t4=Entry(c2,width=12,font='Verdana 12',bg='white',fg='black')
            t4.place(x=465,y=330)

            def like_username():
                bot.like_user(t4.get(),filtration=False)

            def unlike_username():
                bot.unlike_user(t4.get())

            Button(c2, text="Like",font=('Comic Sans MS', 10), width=6, height=1, bg='#00FF00', fg='black', command=like_username).place(x=400,y=370)
            Button(c2, text="Unlike",font=('Comic Sans MS', 10), width=6, height=1, bg='red', fg='white', command=unlike_username).place(x=500,y=370)


            c2.create_text(730,280,text='Follow & Unfollow',font='Verdana 14', fill='white', anchor='nw')
            c2.create_text(700,330,text='Username:',font='Verdana 12', fill='white', anchor='nw')
            t5=Entry(c2,width=12,font='Verdana 12',bg='white',fg='black')
            t5.place(x=815,y=330)

            def follow():
                bot.follow(t5.get())
        
            def unfollow():
                bot.unfollow(t5.get())
        
            Button(c2, text="Follow",font=('Comic Sans MS', 10), width=6, height=1, bg='#00FF00', fg='black', command=follow).place(x=740,y=370)
            Button(c2, text="Unfollow",font=('Comic Sans MS', 10), width=7, height=1, bg='red', fg='white', command=unfollow).place(x=840,y=370)

    b5=Button(c2, text='Login', font=('Comic Sans MS', 10), width=5, height=1, bg='#00FF00', fg='black',command=login).place(x=480,y=160)

    def goback():
        w2.destroy()
        w1.deiconify()

    b4=Button(c2, text='Go Back', font=('Comic Sans MS', 13), width=10, height=1, bg='#FFD11A', fg='black', command=goback).place(x=440,y=520)
    w2.mainloop()

def facebook():
    w1.withdraw()
    w3=Toplevel()
    
    w3.title('Automate Your Facebook!')
    w3width = 1000
    w3height = 600
    x = int((w3.winfo_screenwidth()/2) - (w3width/2))
    y = int((w3.winfo_screenheight()/2) - (w3height/2))
    w3.geometry(f"+{x}+{y}")

    c3 = Canvas(w3, width = 1000, height = 600)      
    c3.pack()

    bg = ImageTk.PhotoImage(Image.open('C:/Users/Neha/Downloads/mini_2A/mini_2A/facebook.jpg'))
    c3.create_image(0, 0, image=bg, anchor='nw')
    
    c3.create_text(250,60,text='Choose the options below to automate',font='Verdana 16', fill='white', anchor='nw')

    def createpost():
        c3.create_text(20,232,text='Username:',font='Verdana 16', fill='white', anchor='nw')
        t1=Entry(c3,width=15,font='Verdana 16',bg='white',fg='black')
        t1.place(x=170,y=232)

        c3.create_text(20,272,text='Password:',font='Verdana 16', fill='white', anchor='nw')
        t2=Entry(c3,show="*",width=15,font='Verdana 16',bg='white',fg='black')
        t2.place(x=170,y=272)

        c3.create_text(20,312,text='Image:',font='Verdana 16', fill='white', anchor='nw')
        t3=Entry(c3,width=15,font='Verdana 16',bg='white',fg='black')
        t3.place(x=170,y=312)

        def browseimg():
            imgdirectory=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (('image files', ('.png', '.jpg')),("all files","*.*")))
            t3.insert(INSERT,imgdirectory)
        
        b7=Button(c3, text='Browse', font=('Comic Sans MS', 10), width=8, height=1, bg='white', fg='#39569C',command=browseimg).place(x=435,y=312)
        
        c3.create_text(20,352,text='Caption:',font='Verdana 16', fill='white', anchor='nw')
        t4=Entry(c3,width=15,font='Verdana 16',bg='white',fg='black')
        t4.place(x=170,y=352)


        def post():
            username=t1.get()
            password=t2.get()
            image=t3.get().replace('/', '\\')
            image=r"{}".format(image)
            sample_comm=['Wonderful!','Great post!','Cheers :)','Nice photography skills!','Wow','Good work','Excellent','Good morning','Have a nice day all!','Yes!','Cool stuff!','What a lovely scene']
            caption=t4.get()
            caption=r"{}".format(caption)
            global driver

            driver=webdriver.Chrome(r'C:\Users\Sonia\OneDrive\Desktop\mini_2A\chromedriver')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_experimental_option("prefs", { \
		        "profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
	        })
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window()
            driver.implicitly_wait(20) # seconds
            driver.get("https://www.facebook.com/")

            elem = driver.find_element(By.ID,"email")
            elem.send_keys(username)
            elem = driver.find_element(By.ID,"pass")
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)

            sleep(5)
            driver.get("https://www.facebook.com/profile.php?id=100073281825777")

            sleep(8)
	
            postarea=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b']"))).click()
            postarea=driver.find_element(By.XPATH, "//div[@class='notranslate _5rpu']")
            sleep(8)

            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Photo/Video']"))
            WebDriverWait(driver, 10).until(element_present).click()
            sleep(2)
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr tgvbjcpo muag1w35 enqfppq2 taijpn5t']"))
            WebDriverWait(driver, 10).until(element_present).click()
            sleep(3)

            pyautogui.write(image, interval=0.25) 
            pyautogui.press('return')
	
            postarea=driver.find_element(By.XPATH, "//div[@class='notranslate _5rpu']")
            postarea.send_keys(caption)
            sleep(6)
	

            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Post']"))
            WebDriverWait(driver, 10).until(element_present).click()
            sleep(6)

            t1.delete(0,END)
            t1.insert(0,'')
            t2.delete(0,END)
            t2.insert(0,'')
            t3.delete(0,END)
            t3.insert(0,'')
            t4.delete(0,END)
            t4.insert(0,'')

            element_present = EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
            WebDriverWait(driver, 10).until(element_present).click()
            sleep(6)

            for i in range(3):
                try:
                    comment=WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Write a comment']/p"))).click();
                    pyautogui.typewrite(random.choice(sample_comm), interval=0.25)
                    pyautogui.press('enter')
                except exceptions.StaleElementReferenceException as e:
                    print(e)
                    pass
            
            sleep(6)
            driver.close()
        b8=Button(c3, text='Post', font=('Comic Sans MS', 10), width=10, height=1, bg='#00FF00', fg='black',command=post).place(x=190,y=402)

    def follow():
        c3.create_text(560,232,text='Username:',font='Verdana 16', fill='white', anchor='nw')
        t5=Entry(c3,width=15,font='Verdana 16',bg='white',fg='black')
        t5.place(x=710,y=232)

        c3.create_text(560,272,text='Password:',font='Verdana 16', fill='white', anchor='nw')
        t6=Entry(c3,show="*",width=15,font='Verdana 16',bg='white',fg='black')
        t6.place(x=710,y=272)

        c3.create_text(560,312,text='Acc Name:',font='Verdana 16', fill='white', anchor='nw')
        t7=Entry(c3,width=15,font='Verdana 16',bg='white',fg='black')
        t7.place(x=710,y=312)

        def clickfollow():
            username=t5.get()
            password=t6.get()
            accname=t7.get()
            accname=r"{}".format(accname)
            global driver

            driver=webdriver.Chrome(r'C:\Users\Neha\Downloads\mini_2A\mini_2A\chromedriver')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_experimental_option("prefs", { \
		        "profile.default_content_setting_values.notifications": 2 # 1:allow, 2:block 
	        })
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window()
            driver.implicitly_wait(20) # seconds
            driver.get("https://www.facebook.com/")

            elem = driver.find_element(By.ID,"email")
            elem.send_keys(username)
            elem = driver.find_element(By.ID,"pass")
            elem.send_keys(password)
            elem.send_keys(Keys.RETURN)

            search = driver.find_element(By.XPATH, "//input[@aria-label='Search Facebook']")
            search.click()
            pyautogui.typewrite(accname, interval=0.25)
            search.send_keys(Keys.RETURN)
            sleep(6)
            follow=WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,  "//div[@aria-label='Follow']")))
            follow.click()
            sleep(6)

            t5.delete(0,END)
            t5.insert(0,'')
            t6.delete(0,END)
            t6.insert(0,'')
            t7.delete(0,END)
            t7.insert(0,'')

            sleep(6)
            driver.close()

        b9=Button(c3, text='Follow', font=('Comic Sans MS', 10), width=10, height=1, bg='#00FF00', fg='black',command=clickfollow).place(x=735,y=362)

    def goback():
        w3.destroy()
        w1.deiconify()

    b5=Button(c3, text='Create A Post', font=('Comic Sans MS', 14), width=13, height=1, bg='white', fg='#39569C',command=createpost).place(x=160,y=160)
    
    b6=Button(c3, text='Follow Account', font=('Comic Sans MS', 14), width=13, height=1, bg='white', fg='#39569C',command=follow).place(x=700,y=160)
    
    b4=Button(c3, text='Go Back', font=('Comic Sans MS', 13), width=10, height=1, bg='white', fg='#39569C', command=goback).place(x=440,y=510)
    w3.mainloop()

def twitter():
    w1.withdraw()
    w4=Toplevel()
    
    w4.title('Automate Your Twitter!')
    w4width = 1000
    w4height = 600
    x = int((w4.winfo_screenwidth()/2) - (w4width/2))
    y = int((w4.winfo_screenheight()/2) - (w4height/2))
    w4.geometry(f"+{x}+{y}")

    c4 = Canvas(w4, width = 1000, height = 600)      
    c4.pack()

    bg = ImageTk.PhotoImage(Image.open('C:/Users/Neha/Downloads/mini_2A/mini_2A/twitter.jpg'))
    c4.create_image(0, 0, image=bg, anchor='nw')

    c4.create_text(250,60,text='Enter the details below to automate',font='Verdana 16', fill='white', anchor='nw')

    c4.create_text(300,172,text='Username:',font='Verdana 16', fill='white', anchor='nw')
    t1=Entry(c4,width=15,font='Verdana 16',bg='white',fg='black')
    t1.place(x=450,y=172)

    c4.create_text(300,212,text='Password:',font='Verdana 16', fill='white', anchor='nw')
    t2=Entry(c4,show="*",width=15,font='Verdana 16',bg='white',fg='black')
    t2.place(x=450,y=212)

    c4.create_text(300,252,text='Message:',font='Verdana 16', fill='white', anchor='nw')
    t3=Entry(c4,width=15,font='Verdana 16',bg='white',fg='black')
    t3.place(x=450,y=252)

    c4.create_text(300,292,text='Image:',font='Verdana 16', fill='white', anchor='nw')
    t4=Entry(c4,width=15,font='Verdana 16',bg='white',fg='black')
    t4.place(x=450,y=292)

    def browseimg():
        imgdirectory=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (('image files', ('.png', '.jpg')),("all files","*.*")))
        t4.insert(INSERT,imgdirectory)
        
    b7=Button(c4, text='Browse', font=('Comic Sans MS', 10), width=8, height=1, bg='white', fg='#39569C',command=browseimg).place(x=720,y=292)

    def tweet():
        username=t1.get()
        password=t2.get()
        #phone=
        message=t3.get()
        message=r"{}".format(message)
        image=t4.get().replace('/', '\\')
        image=r"{}".format(image)
        driver=webdriver.Chrome(r'C:\Users\Sonia\OneDrive\Desktop\mini_2A\chromedriver')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)

        driver.get("https://twitter.com/login")
        sleep(3)

        email_xpath='//input[@name="username"]'
        #email_xpath='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        email_next_xpath='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span'
        #phn_no_xpath='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        #phn_no_next='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span'
        password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input'
        login_xpath = '//div[@role="button"]'
        sleep(3)

        element=driver.find_element_by_xpath(email_xpath)
        sleep(3)
        element.send_keys(username)
        sleep(3)
        driver.find_element_by_xpath(email_next_xpath).click()
        sleep(3)
        #element=driver.find_element_by_xpath(phn_no_xpath)
        #sleep(3)
        #element.send_keys(phone)
        #sleep(3)
        #driver.find_element_by_xpath(phn_no_next).click()
        #sleep(3)
        element=driver.find_element_by_xpath(password_xpath)
        sleep(3)
        element.send_keys(password)
        sleep(3)
        element.send_keys(Keys.RETURN)
        #driver.find_element_by_xpath(login_xpath).click()
        sleep(5)

        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span'
        message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        media_xpath='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div'
        post_tweet_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span'

        sleep(4)

        driver.find_element_by_xpath(tweet_xpath).click()
        sleep(0.5)
        driver.find_element_by_xpath(message_xpath).send_keys(message)
        sleep(3)
        driver.find_element_by_xpath(media_xpath).click()
        sleep(3)
        pyautogui.write(image, interval=0.25) 
        pyautogui.press('return')
        sleep(3)
        driver.find_element_by_xpath(post_tweet_xpath).click()
        sleep(10)

        driver.close()
        t1.delete(0,END)
        t1.insert(0,'')
        t2.delete(0,END)
        t2.insert(0,'')
        t3.delete(0,END)
        t3.insert(0,'')
        t4.delete(0,END)
        t4.insert(0,'')
        

    b5=Button(c4, text='Tweet!', font=('Comic Sans MS', 10), width=10, height=1, bg='#00FF00', fg='black',command=tweet).place(x=455,y=362)

    def goback():
        w4.destroy()
        w1.deiconify()

    b4=Button(c4, text='Go Back', font=('Comic Sans MS', 13), width=10, height=1, bg='white', fg='#1A75FF', command=goback).place(x=440,y=500)
    w4.mainloop()


b1=Button(c1, text='Instagram', font=('Comic Sans MS', 14), width=10, height=1, bg='#FF4DD2', fg='white', command=instagram).place(x=120,y=420)
b2=Button(c1, text='Facebook', font=('Comic Sans MS', 14), width=10, height=1, bg='#39569C', fg='white', command=facebook).place(x=420,y=420)
b3=Button(c1, text='Twitter', font=('Comic Sans MS', 14), width=10, height=1, bg='#1A75FF', fg='white', command=twitter).place(x=720,y=420)    
w1.mainloop()





