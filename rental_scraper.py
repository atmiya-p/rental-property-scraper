from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from time import sleep;
from selenium.webdriver.common.by import By

def construct_towns_and_cities_list(file_name):
    towns_cities_list = []
    with open(file_name) as file:
        for line in file:
            towns_cities_list.append(line.rstrip().lower())

    return towns_cities_list


# Make sure to change path to where the chromedriver is located
PATH = "/Users/atmiyapatel/Downloads/chromedriver"
service = Service(PATH)
driver = webdriver.Chrome(service= service)

# We will use realtor.ca as it is Canada's largest real estate website
final_towns_cities_list = construct_towns_and_cities_list('ontario_towns_cities')
while True:
    rentalCity = input("What city are you interested in renting?: ")
    if rentalCity.lower() in final_towns_cities_list:
        print("Found city/town")  # For test purposes
        break

    else:
        print("Sorry it seems that this city/town is not in the list of Ontario cities. Please double check if it is a valid city, and if is then feel free to add to the txt file! If not, feel free to try again ")


rental_url = f"https://www.realtor.ca/on/%s/rentals?gad_source=1&gclid=CjwKCAjwk8e1BhALEiwAc8MHiBzxtq0DWgB_kAFSDjUIoX2ahmeN9LhAnZ_9AW9nsadbTZzZk4QBrRoCAE0QAvD_BwE", rentalCity.replace(" ", "")

driver.get(rental_url)

sleep(5)  # 5 seconds for it to load

# initializing list for the properties
properties_list = []

# <div class="listingCard card">
property = driver.find_elements(By.CLASS_NAME, 'listingCard')

