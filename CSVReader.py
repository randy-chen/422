'''
CSVReader.py

Created by Cody Abe on 04/13/17
Copyright © 2017 Cody Abe. All rights reserved.

'''
import csv

def read_csv():
    with open('testCSV.csv', 'r') as csvfile:
        students = csv.reader(csvfile, delimiter=',', quotechar='"')
        array = []
        for row in students:
            array.append(row) #putting array into another array (just to print out at the end)
        return array

def parse_categories(csv_array):
    categories_array = csv_array.pop(0)
    categories_dict = {}
    for i in range(len(categories_array)):
        categories_dict[i] = categories_array[i]
    return categories_dict

def parse_student(student, categories_dict):
    count = len(categories_dict)
    student_string = ''
    for i in range(count):
        if(i == 0):
            student_string += student[i]
            student_string += ' '
        else:
            student_string += student[i]
            student_string += '\n'
    return student_string

def main():
    final_string = ''
    csv = read_csv()
    categories = parse_categories(csv)
    category_count = len(categories)
    final_string += str(category_count - 2)
    final_string += '\n'
    for row in csv:
        final_string += parse_student(row, cat)

    text_file = open("output.txt", "w")
    text_file.write(final_string)
    text_file.close()

if __name__ == "__main__":
    main()
