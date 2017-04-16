'''
CSVReader.py

Created by Cody Abe on 04/13/17
Copyright © 2017 Cody Abe. All rights reserved.

'''
import csv

class Student:
    '''
    This is a class for and object student with various attributes
    '''

    def __init__(self, _first, _last):
        self.first = _first
        self.last = _last
        self.schedule = []
        self.languages = []

    def update_schedule():
        '''
        todo: implement this function
        '''
    def update_languages():
        '''
        todo: implement this function
        '''

def read_csv():
    with open('testCSV.csv', 'r') as csvfile:
        students = csv.reader(csvfile, delimiter=',', quotechar='"')
        array = []
        for row in students:
            array.append(row) #putting array into another array (just to print out at the end)
        return array

def parse_categories(csv_array):
    categories_dict = {}
    for i in range(len(csv_array[0])):
        categories_dict[csv_array[0][i]] = i

    print (csv_array)
    print (categories_dict, categories_dict['Last'])



def main():
    read_csv()
    parse_categories(read_csv())

if __name__ == "__main__":
    main()
