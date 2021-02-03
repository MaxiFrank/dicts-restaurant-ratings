import sys
import random

file = sys.argv[1]

def read_file(file):
    """reads file and return a list of strings"""
    with open(file, 'r') as read_file:
        dict_ = {}
        for line in read_file:
            line = line.rstrip().split(":")
            dict_[line[0]] = int(line[1])
    return dict_

def restaurant_rating(dict_):
    """Restaurant rating lister."""
    for key in sorted(dict_):
        print(f'{key} is rated at {dict_[key]}.')


def get_user_input(file, dict_):
    while True:
        print("Here's what you can do:")
        print("(1) See all the ratings")
        print("(2) Add a new restaurant")
        print("(3) Quit")
        print("(4) Updated random restaurant rating")
        choice = input("What would you like to do? ")

        if choice == "3":
            print("Goodbye")
            break
        elif choice == "1":
            restaurant_rating(dict_)
        elif choice == "2":
            while True:
                restaurant_name = input('Please enter the name of a new restaurant ')
                rating = int(input(f'Please enter the score of {restaurant_name} '))
                if rating < 1:
                    print("Invalid input")
                    # rating = int(input(f'Please enter the score of {restaurant_name} '))
                elif rating > 5:
                    print("Invalid input")
                    # rating = int(input(f'Please enter the score of {restaurant_name} '))
                elif rating >= 1 and rating <= 5:
                    dict_[restaurant_name] = rating
                    break
        elif choice == "4":
            selected_restaurant = random.choice(list(dict_.keys()))
            print(f'{selected_restaurant} is rated at {dict_[selected_restaurant]}.')
            while True:
                new_rating = int(input(f'Please enter the score of {selected_restaurant} '))
                if new_rating < 1:
                    print("Invalid input")
                    # rating = int(input(f'Please enter the score of {restaurant_name} '))
                elif new_rating > 5:
                    print("Invalid input")
                    # rating = int(input(f'Please enter the score of {restaurant_name} '))
                elif new_rating >= 1 and new_rating <= 5:
                    dict_[selected_restaurant] = new_rating
                    break

    return restaurant_name, rating

dict_ = read_file(file)
get_user_input(file, dict_)