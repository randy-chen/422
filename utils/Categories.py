'''
CSVReader.py

Created by Cody Abe on 04/13/17
Copyright © 2017 Cody Abe. All rights reserved.

'''
import csv
import sys

def read_csv(csv_input):
    '''
    Usage: To create an array of students that will be parsed later.
    arg: Input in the form of a csv file
    returns: an array of students
    '''
    with open(csv_input, 'r') as csvfile:
        students = csv.reader(csvfile, delimiter=',', quotechar='"') #creates correct format of csv
        array = []
        for row in students:
            array.append(row) #putting array into another array (just to print out at the end)
        return array

def parse_categories(csv_array):
    '''
    Usage: To create an array of categories in order to be output into the final
    text file.
    arg: the array from the read_csv function
    returns: a dictionary of categories
    '''
    categories_array = csv_array.pop(0)
    categories_dict = {}
    for i in range(len(categories_array)):
        categories_dict[i] = categories_array[i]
    return categories_dict

def main(csv_input):
    final_string = ''
    csv = read_csv(csv_input)
    categories = parse_categories(csv)
    for item in categories:
        if not (item == 0 or item == 1):
            final_string += (categories[item] + "\n")


    text_file = open("categories.txt", "w")
    text_file.write(final_string)
    text_file.close()

if __name__ == "__main__":
    print(sys.argv[1])
    main(sys.argv[1])
