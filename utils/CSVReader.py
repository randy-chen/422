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
        students = csv.reader(csvfile, delimiter=',', quotechar='"')  #creates correct format of csv
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

def parse_student(student, categories_dict):
    '''
    Usage: To create an array of students that will be parsed later.
    arg:
        student: This is the array after parse_categories
        categories_dict: This is the dictionary of categories from parse_categories
    returns: a string of students
    '''
    count = len(categories_dict)
    student_string = ''
    for i in range(count):
        if(i == 0): #if its the name so the first and last name can be on the same line
            student_string += student[i]
            student_string += ' '
        else: #puts the categories on new lines
            student_string += student[i]
            student_string += '\n'
    return student_string

def main(file_input):
    final_string = ''
    csv = read_csv(file_input)
    categories = parse_categories(csv)
    category_count = len(categories)
    final_string += str(category_count - 2)
    final_string += '\n'
    for row in csv:
        final_string += parse_student(row, categories)

    text_file = open("output.txt", "w")
    text_file.write(final_string)
    text_file.close()

if __name__ == "__main__":
    main(sys.argv[1])
