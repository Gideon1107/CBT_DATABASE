#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:47:21 2022

@author: gideon
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:11:15 2022

@author: gideon
"""
# Which of this is the capital of Nigeria?\n(a) Lagos\n(b)Kano\n(c)Abuja
# What is the number of states in Nigeria?\n(a)37\n(b)36\n(c)44','b'],
# What is the number of LGAs in Nigeria?\n(a)768\n(b)774\n(c)780','b'],
# Who is INEC chairman?\n(a)Prof Mamhood Yakubu\n(b)Prof Wole Soyinka\n(c)Prof Adeyami Paul','a'],
# How many political parties participated in the 2019 presidential election?\n(a)18\n(b)77\n(c)73','c']}

# query = "ALTER TABLE admin_base AUTO_INCREMENT = 1"
# mycursor.execute(query)
# mycon.commit()


import sys
import mysql.connector
mycon = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", database= "Newcbt")
mycursor = mycon.cursor()



class program_admin():
    
    def __init__(self):
        self.welcome()
        
    def welcome(self):
        print("\n")
        print("Welcome")
        print("To login press 1. \nTo Register as an admin press 2.\nTo exit press 3.")
        admin_input = str(input("Enter option: "))
        if admin_input == "1":
            self.login_admin()
        elif admin_input == "2":
            self.reg_admin()
        elif admin_input == "3":
            sys.exit()
    def reg_admin(self):
        self.admin_id = input("Enter preferred admin name: ")
        self.admin_pass = input("Enter preferred password: ")
        get_admin_id = "INSERT INTO admin_base (admin_id, admin_pass) VALUES(%s, %s)"
        reg = (self.admin_id,self.admin_pass)
        mycursor.execute(get_admin_id,reg)
        mycon.commit()
        print("Registration successful")
        self.welcome()
    
    def login_admin(self):
        self.log_admin_id = input("Enter your admin name:")
        self.log_admin_pass = input("Enter password:")
        log_admin = "SELECT admin_id,admin_pass FROM admin_base WHERE admin_id = %s AND admin_pass = %s"
        login = (self.log_admin_id, self.log_admin_pass,)
        mycursor.execute(log_admin,login)
        admin_base = mycursor.fetchone()
        if admin_base:
            print("\n")
            print("Login successful"),print("Welcome,",self.log_admin_id)
            self.admin_page()
        else:
            print("incorrect id/pass try again")
            self.login_admin()
            
    def admin_page(self):
        print("==========================")
        print("To set new questions press 1.\nTo delete existing question press 2.\nTo logout press 3.")
        admin_input = str(input("Enter operation: "))
        if admin_input == "1":
            self.setquestion()
        elif admin_input == "2":
            self.delquestion()
        elif admin_input == "3":
            
            sys.exit()
        
    def setquestion(self):
        self.questions = input('Enter new question: ')
        self.option_a = input('Enter option A: ')
        self.option_b = input('Enter option B: ')
        self.option_c = input('Enter option C: ')
        self.option_d = input('Enter option D: ')
        self.correct_option = input('Enter correct option: ')
        myquery = "INSERT INTO question (questions, option_a,option_b,option_c,option_d, correct_option) VALUES(%s, %s, %s,%s,%s,%s)"
        newquestion = (self.questions,self.option_a,self.option_b,self.option_c,self.option_d,self.correct_option)
        mycursor.execute(myquery, newquestion)
        mycon.commit()
        print(mycursor.rowcount, "question(s) inserted successfully")
        self.admin_page()
        
        
    def delquestion(self):
        delete ="DELETE FROM question WHERE questions = %s"
        quest = input("Enter the question to be deleted\n:")
        delet = (quest,)
        mycursor.execute(delete, delet)
        mycon.commit()
        print(mycursor.rowcount, 'question(s) deleted successfuly')
        self.admin_page()
        
    
c = program_admin()