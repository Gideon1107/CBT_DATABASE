#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:11:33 2022

@author: gideon
"""
import sys
import mysql.connector
mycon = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", database= "Newcbt")
mycursor = mycon.cursor()





class program_user():
    def __init__(self):
        self.welcome_user()
     
    #FOR USER REGISTRATION
    def reg_user(self):
          self.user_id = input("Enter preferred user name: ")
          self.user_pass = input("Enter preferred password: ")
          get_user_id = "INSERT INTO user_base (user_id, user_pass) VALUES(%s, %s)"
          reg_user = (self.user_id,self.user_pass)
          mycursor.execute(get_user_id,reg_user)
          mycon.commit()
          print("Registration successful")
          self.welcome_user()
    
    #THIS FUNCTION LOG IN USER
    def login_user(self):
        self.log_user_id = input("Enter your user name: ")
        self.log_user_pass = input("Enter password: ")
        log_user = "SELECT user_id,user_pass FROM user_base WHERE user_id = %s AND user_pass = %s"
        login = (self.log_user_id, self.log_user_pass,)
        mycursor.execute(log_user,login)
        user_base = mycursor.fetchone()
        if user_base:
            print("\n")
            print("Login successful"),print("Welcome,",self.log_user_id)
            self.user_page()
        else:
            print("incorrect id/pass try again")
            self.login_user()
            
    def welcome_user(self):
        print("\n")
        print("Welcome")
        print("To login press 1. \nTo Register as a user press 2.\nTo exit press 3.")
        user_input = str(input("Enter option: "))
        if user_input == "1":
            self.login_user()
        elif user_input == "2":
            self.reg_user()
        elif user_input == "3":
            sys.exit()
            
            
    def user_page(self):
        print("press 1 to begin the test")
        user_input = str(input("Enter option: "))
        if user_input == "1":
            self.user_question()
     
    #TO FETCH QUESTION AND OPTIONS FROM D DATABASE
    def user_question(self):
        display = "SELECT * FROM question"
        mycursor.execute(display)
        output = mycursor.fetchall()
        if output:
            score = 0
            for i in output:
              print("Question",i[0])
              print(i[1])
              print(i[2])
              print(i[3])
              print(i[4])
              print(i[5])
              ans = input("Enter answer: ")
              if i[-1] == ans:
                  score += 5
              else:
                  pass
        print("Dear",self.log_user_id,",","your total is",score, "out of 25")
        print("Thank you for taking the test, Enter 0 to sign out")
        out = str(input(">: "))
        if out == "0":
         sys.exit()
              
                  
u = program_user() 
     
    




