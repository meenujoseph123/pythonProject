# Import Library
#import By as By
from robot.libraries import String
from selenium import webdriver
import time

# set webdriver path here it may vary
# It's the location where you have downloaded the ChromeDriver
driver = webdriver.Chrome(executable_path=r"C:\\chromedriver.exe")

# Get the target URL
driver.get('https://html.com/tags/button/')

# Wait for 5 seconds to load the webpage completely
time.sleep(5)

# Find the button using text
driver.find_element_by_xpath('//button[normalize-space()="Click me!"]').click()

time.sleep(5)

# Close the driver
driver.close()

# verify button text is “Dispense Now”......................................................................

#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Create a button
button= ttk.Button(win, text="My Button")
button.pack()
#Get the text of Button
mytext= button.cget('text')
#Create a label to print the button information
Label(win, text=mytext, font='Helvetica 20 bold').pack(pady=20)
win.mainloop()

### verify color of button is red..........................................................................................

driver.get("https://getbootstrap.com/docs/4.0/components/buttons/")

btn_list = driver.find_elements_by_xpath("//div[@class = 'bd-example'][1]/button")

for itm in range(0, len(btn_list)):
    name = btn_list[itm].text
    print(name)
    color = btn_list[itm].value_of_css_property("backgroundColor")
    print(color)

    if color == "rgba(0, 123, 255, 1)":# do any action
        print("Button with Primary color detected")


# verify a page with success message displayed after clicked on “Dispense Now” button........................................................
# import module


# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Chrome(r"./driver/chromedriver")

# get https://www.geeksforgeeks.org/
driver.get("https://www.geeksforgeeks.org/")

# Maximize the window and let code stall
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(10)

# Obtain button by link text and click.
button = driver.find_element_by_link_text("Sign In")
button.click()
time.sleep(100)
#String bodyText = driver.findElement(By.tagName("body")).getText()
#AssertionError.assertTrue("“Cash dispensed”", bodyText.contains(bodyText))