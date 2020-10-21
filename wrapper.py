import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sendEmail import sendEmail
from checkJobOffer import scrapeOffer, checkNewOffer
import pickle

if __name__ == "__main__":
        #Don't forget to change the url and your driverPath.
        url = "https://www.civiweb.com/FR/offre-recherche-avancee/Page/1.aspx?q=s=@c=2,@a=@e=@m=@f=@r=@v=@t="
        driverPath = "/Users/henriterrasse/Code/ChromeDriver/chromedriver"
        scrapeOffer(driverPath, url)
        checkNewOffer()