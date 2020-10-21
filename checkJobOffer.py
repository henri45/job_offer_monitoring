import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sendEmail import sendEmail
import pickle

def scrapeOffer(driverPath, url):
    #The headless argument permits to start ChromeDriver without opening the window.
    #It can be useful if you run the script locally and don't want to be bothered by the automatic opening of the webdriver.
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome(driverPath, options = chrome_options)

    #Initialisation of the selenium webdriver
    driver = webdriver.Chrome(driverPath)
    
    #Go to the webpage we want to scrape
    driver.get(url)

    #Collect the element with the following class.
    jobOffers = driver.find_elements_by_class_name('xt_offrelink')

    #Extract the text from the element. These are the job titles
    jobOffers = [offer.text for offer in jobOffers]
    driver.close()

    #Save the array in a pickle format.
    pickle.dump(jobOffers, open("listNewOffers.pickle", "wb"))

def checkNewOffer():
    #Load yesterday's offers
    listOldOffers = pickle.load(open("listOldOffers.pickle", "rb"))

    #Load today's offers
    listNewOffers = np.array(pickle.load(open("listNewOffers.pickle", "rb")))

    #isNew checks if the offer were already there yesterday.
    isNew = np.array([newOffer not in listOldOffers for newOffer in listNewOffers])

    #If there is a new offer...
    if any(isNew):
        newOffers = listNewOffers[isNew]
        for newOffer in newOffers:
            #...Send an email with the name of the new offers.
            sendEmail(newOffer)

    #Update the old offer array
    pickle.dump(listNewOffers, open("listOldOffers.pickle", "wb"))