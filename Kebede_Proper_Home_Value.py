"""Proper Home Value Calculator Python Script for INST326

Driver: Kerubel Kebede
Navigator: None
Assignment: Final Project
Date: 11/29/2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~
"""


import sys
import argparse
import csv

class value:

    location = input('Where is the location of the house: ')

    def __init__(self, location):
        self.location = location  
   
   
    def home_location(self.location):
            '''
            Args: 
            location(str): The adress/city of the house
            Function: 
            This function takes the location/city entered and searches a database list of
            homes in the entered location. 
            '''
            print(self.location)

    def home_info(self, doors, windows, square_footage , age, estimate_price):
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
            

            per_squarefootage = 100
            per_numofdoors = 1100
            per_numofwindows = 840
            per_year_for_age = 1470
            doors = input('How many doors are in the house: ')
            windows = input('How many windows are in the house: ')
            square_footage = input('What is the square footage of the house: ')
            age = input('How old is the house: ')

            self.doors = doors
            self.windows = windows
            self.square_footage = square_footage
            self.age = age

            square_footage_price = square_footage * per_squarefootage 
            doors_price = doors * per_numofdoors
            windows_price = windows * per_numofwindows
            house_years_price = age * per_year_for_age

            estimate_price = square_footage + doors_price + windows_price + house_years_price

            return estimate_price

            

    def home_recommendation(self, location, price, recommendation):
            '''
            Args:
            location(str): holds the desired location/city
            price(int): holds the prefered price range entered by the user
            recommendation(list): holds the list of homes recommended in the location entered by the user
            Function: 
            This function takes the desired location/city, prefered price range and mathes it with location and price ranges in a database
            and returns the results. 
            '''
            price = input('Enter your preferred price range: ')
            print(price)
            #working on this function
            
    def main(estimate_price, recommendation):
            '''
            Args: 
            estimate_price(float): holds the estimate price of the home
            recommendation(list): holds a list of recommended homes from database
            Function:
            This function returns the estimate price after the calculation and the recommended homes 
            in the area chosen by the user. 
            '''
            #Code goes here

    def parse_args(args_list):
            '''Takes a list of strings from the command prompt and passes them through as arguments

            Args:
                args_list(list): the list of strings from the command prompt
            Returns:
                args (ArgumentParser)
            
            '''

            parser = argparse.ArgumentParser()
            parser.add_argument('estimate_price', type = float, help = 'holds the estimate price of a home based on the attributes entered.')
            parser.add_argument('recommendation', type = list, help = 'holds the list of recommended homes in the locatin entered.')

            args = parser.parse_args(args_list)

            return args