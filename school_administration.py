# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:42:15 2023

@author: g_sha
"""
import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
        writer.writerow(info_list)

if __name__ == '__main__':
    con = True
    student_num = 1
    
    while con:
        student_info = input("Enter student information in the following format (Name Age Contact_Number Email_ID): ")
        print("Entered information: " + student_info)
        
        student_info_list = student_info.split(' ')
        print("Entered split up information is: " + str(student_info_list))
        
        choice_check = input("Is the entered information correct? (yes/no): ")
        if choice_check == "yes":
            write_into_csv(student_info_list)
            
            con_check = input("Do you want to enter information for another student? (y/n): ")
            if con_check == "y":
                con = True
                student_num += 1
            elif con_check == "n":
                con = False
        elif choice_check == "no":
            print("Please re-enter the values.")
