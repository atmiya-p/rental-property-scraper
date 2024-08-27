import pandas as pd
from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from time import sleep;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def construct_towns_and_cities_list(file_name):
    towns_cities_list = []
    with open(file_name) as file:
        for line in file:
            towns_cities_list.append(line.rstrip().lower())

    return towns_cities_list


def get_scraped_properties():
    sleep(15)  # 5 seconds for it to load

    # <div class="listingCard card">
    propertyCards = driver.find_elements(By.CLASS_NAME, 'listingCard')

    for rentalProperty in propertyCards:
        property_info = {}

        # <div class="listingCardAddress" data-binding="innertext=Address"> ADDRESS WOULD BE HERE </div>
        try:
            address_element = rentalProperty.find_element(By.CLASS_NAME, 'listingCardAddress')
            if address_element:
                property_info['address'] = address_element.text
            else:
                property_info['address'] = "N/A"
        except Exception as exception:
            property_info['address'] = "Could not locate"
            print(exception)

        print(address_element.text)

        # <div class="listingCardPrice" title="$0,000/Monthly" data-value-cad="$0,000/Monthly" data-binding="hidden=ListingIsSold,data-value-cad={Price},innertext=DisplayPrice,title=ConvertedPrice">$0,000/Monthly</div>
        try:
            price_element = rentalProperty.find_element(By.CLASS_NAME, 'listingCardPrice')
            if price_element:
                property_info['price'] = price_element.text
            else:
                property_info['price'] = "N/A"
        except Exception as exception:
            property_info['price'] = "Could not locate"
            print(exception)

        print(price_element.text)

        try:
            listingCardIconTopCons = rentalProperty.find_elements(By.CLASS_NAME, 'listingCardIconCon')
            for listingCardIconTopCon in listingCardIconTopCons:
                if listingCardIconTopCon.find_element(By.CLASS_NAME, 'listingCardIconText').text.strip() == 'Bedrooms':
                    property_info['bedrooms'] = listingCardIconTopCon.find_element(By.CLASS_NAME, 'listingCardIconNum').text.strip()

                elif listingCardIconTopCon.find_element(By.CLASS_NAME, 'listingCardIconText').text.strip() == 'Bathrooms':
                    property_info['bathrooms'] = listingCardIconTopCon.find_element(By.CLASS_NAME, 'listingCardIconNum').text.strip()
        except Exception as exception:
            print(exception)
            property_info['bedrooms'] = 'N/A'
            property_info['bathrooms'] = 'N/A'

        print(property_info['bedrooms'])
        print(property_info['bathrooms'])

        properties_list.append(property_info)


def statistical_analysis(properties_dictionary):
    for properties in properties_dictionary:
        properties['price'] = int(properties['price'].replace('$', '').replace(',', '').split('/')[0])


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


rental_url = f"https://www.realtor.ca/on/{rentalCity.replace(' ', '')}/rentals?gad_source=1&gclid=CjwKCAjwk8e1BhALEiwAc8MHiBzxtq0DWgB_kAFSDjUIoX2ahmeN9LhAnZ_9AW9nsadbTZzZk4QBrRoCAE0QAvD_BwE"

print(rental_url)  # test to see link

driver.get(rental_url)

# initializing list for the properties
properties_list = []

get_scraped_properties()
print(properties_list)

df = pd.DataFrame(properties_list)
print(df)
file_name = f"{rentalCity}_rental_properties.xlsx"
df.to_excel(file_name, index=False)
print(f"{file_name} has been saved")

statistical_analysis(properties_list)

''''
def go_next():
    wait = WebDriverWait(driver, 30)
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.lnkNextResultsPage.paginationLink.paginationLinkForward.btn.small")))
        if "disabled" in next_button.get_attribute("class"):
            print("Next button is not clickable anymore")
            return False
        next_button.click()
        sleep(5)  # Allow time for the next page to load
        return True
    except Exception as e:
        print("Exception while locating the next button:", e)
        return False


while True:
    if go_next():
        get_scraped_properties()
    else:
        break

'''
