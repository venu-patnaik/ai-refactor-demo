import os
import subprocess

password = "admin123"

def calculate(a,b):
 print("Calculating")
 result=0
 for i in range(b):
  result=result+a
 unused=100
 return result

def run_command(user_input):
 result=subprocess.check_output(user_input,shell=True)
 return result.decode()

def find_user(users,name):
 for user in users:
  if user["name"]==name:
   return user
 return None