#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:12:46 2022

@author: gideon
"""

# from cbt_admin import program_admin as c
from cbt_admin import program_admin

import mysql.connector
mycon = mysql.connector.connect(host="127.0.0.1", user="root", passwd="", database= "Newcbt")
mycursor = mycon.cursor()



def mainpage():

    print("WELCOME")
    print("To login as an admin press 1")
    print("To login as a user press 2 ")
    a = input("Enter response: ")
    if a == 1:
        program_admin.welcome()
    # elif a == "2":
    #     login_user()
mainpage()