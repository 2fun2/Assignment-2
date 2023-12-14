#!/usr/bin/env python3

import subprocess, sys
import os
import argparse

'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: "Soheil Jafari"
The python code in this file (duim.py) is original work written by
"Soheil Jafari. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: Improved du

Date: 12/11/2023
''' 


 # Create an ArgumentParser
def setup_parser():#defining a function
    #adding argument for directory and then return parser
    parser = argparse.ArgumentParser(description="File search and report script.")#creating the parser option
    parser.add_argument('--directory', type=str, required=True, help='Target directory for searching files.')#specifying the directory
    parser.add_argument('--criteria', nargs='+', required=True, help='Criteria for file search.')
  return parse


def percent_to_graph(percent, total_chars):

 # Convert a percentage value
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be between 0 and 100")
    filled_chars = int(round(percent / 100 * total_chars))
    return '=' * filled_chars + ' ' * (total_chars - filled_chars)


def call_du_sub(location):
    try:
     #call the 'du' command
        result = subprocess.check_output(["du", "-d", "1", location], text=True)
        # Split the result 
        return result.strip().split('\n')
    except subprocess.CalledProcessError as e:
        # Handle any errors  and stop
        print(f"An error occurred: {e}")
        return []


# Create a dictionary for du commad
def create_dir_dict(du_list):
    dir_dict = {}
    for line in du_list:
        parts = line.split()
        if len(parts) == 2:
            dir_dict[parts[1]] = int(parts[0])
    return dir_dict

