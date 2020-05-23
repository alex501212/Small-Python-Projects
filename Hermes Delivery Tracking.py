from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

def track():
    global entry
    trackingNo = entry.get()

    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome("C:\chromedriver.exe", options=chromeOptions)

    driver.get("https://international.myhermes.co.uk/tracking")
    trackBox = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div[1]/div/div/form/div/div[1]/input")
    trackBox.send_keys(trackingNo)

    trackSearch = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[5]/div/div[1]/div/div/form/div/div[2]/input")
    trackSearch.click()

    deliveryDue = driver.find_element_by_xpath(
        "/html/body/div[2]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/span[2]")
    deliveryDue = deliveryDue.text

    trackStatus.config(text=deliveryDue)
    driver.quit()

root = Tk()
root.title("Hermes Parcel Tracking")

trackNo = Label(root, text="Enter Your Tracking Number: ")
trackNo.grid(row=0)

trackStatusLabel = Label(root, text="Tracking Status: ")
trackStatusLabel.grid(row=1, sticky="w")

trackStatus = Label(root, text="")
trackStatus.grid(row=1, column=1, sticky="w")

entry = Entry(root)
entry.grid(row=0, column=1)
entry.focus_set()

button1 = Button(root, text="Submit", command=track)
button1.grid(row=0, column=2)

root.mainloop()
