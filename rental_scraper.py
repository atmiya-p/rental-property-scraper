from selenium import webdriver;
from time import sleep;
from selenium.webdriver.common.by import By

# Make sure to change path to where the chromedriver is located
PATH = "/Users/atmiyapatel/Downloads/chromedriver"
driver = webdriver.Chrome(PATH);

# We will use realtor.ca as it is Canada's largest real estate website
rental_url = "www.realtor.ca"

