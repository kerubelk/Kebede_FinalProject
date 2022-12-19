"""Proper Home Value Calculator Python Script for INST326

Driver: Kerubel Kebede
Navigator: None
Assignment: Final Project
Date: 11/29/2022

Challenges Encountered: After the code for webscraping, which is(home_reccomendation) function is executed, the display does not stay on but closes. 
"""
import math 

  

def proper_value_calculation(doors, windows, square_footage, age):
            '''
            Args:
            doors(int): this holds the number of doors(rooms) in the house.
            windows(int): this holds the number of windows in the house
            size(int): the square footage of the house
            age(int): this holds the age of the house
            estmate_price(float): holds the estimated price for the home
            Function:
            This function takes the attributes of the house(size, windows, doors, and age)
            and gives an estimate on the proper value of the home. 
            '''
            
            #The prices for the attributes of the house
            square_footage_price = square_footage * 100 
            doors_price = doors * 1100
            windows_price = windows * 840
            house_years_price = age * 1470
            
            #calculation for the estimation of the home value
            estimate_price = square_footage_price + doors_price + windows_price + house_years_price
            print("estimate price: ", estimate_price)
           
            return estimate_price   #return the estimate price for the house

            

            

def home_recommendation():
            '''
            Args:
            location(str): holds the desired location/city
            price(int): holds the prefered price range entered by the user
            recommendation(list): holds the list of homes recommended in the location entered by the user
            Function: 
            This function takes the desired location/city, prefered price range and mathes it with location and price ranges in a database
            and returns the results. 
            '''
            #import the proper modules for selenium
            from selenium import webdriver
            from selenium.webdriver.support.ui import Select
            from selenium.webdriver.common.by import By
            
            #url for the website
            website = "https://www.newhomesource.com/mls_com"
            
            path = r'"\Users\kerub\Downloads\chromedriver_win32.zip"'
            #the prefered location for the house
            location = input("Enter a location: ")
            #variable that connects between the chrome path and website
            driver = webdriver.Chrome(path)
            #fetch the website for the new homes list
            driver.get(website)

            #finds the element where the location can be entered in the website
            search = driver.find_element(By.NAME, "SearchText")

            #sends the location entered by the user to the website
            search.send_keys(location)

            #finds the element of the search button
            search_button = driver.find_element(By.ID, "HomeSearchBtn")
            #clicks the search button
            search_button.click()
            
            
def main():
        #gets the attributes of the house from the user
        doors = int(input('How many doors are in the house: '))
        windows = int(input('How many windows are in the house: '))
        square_footage = int(input('What is the square footage of the house: '))
        age = int(input('How old is the house: '))
        
        #calls the function to do the calculation of the estimation price for the house
        proper_value_calculation(doors, windows, square_footage, age)

        #asks the user if they would like to look at homes list in a specific location
        reccomendation = input("Would you like to search for homes in you're prefered location: ")
        
        #if the user enters yes, home_recommendation function is called
        if (reccomendation == 'yes'):
            home_recommendation()
        else:
            print("Thank you for using my program:") #if the user enters no, the program ends
            
            
if __name__ == "__main__":
    main()
