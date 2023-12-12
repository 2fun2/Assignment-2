#!/usr/bin/env python3

import subprocess, sys
import os
import argparse

'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: "Student Name"
The python code in this file (duim.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 
'''


def parse_command_args():
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Display sizes in a human-readable format")
    parser.add_argument("target", nargs=1, help="Target directory for disk usage analysis")
    return parser.parse_args()

def percent_to_graph(percent, total_chars):
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be between 0 and 100")
    filled_chars = int(round(percent / 100 * total_chars))
    return '=' * filled_chars + ' ' * (total_chars - filled_chars)


def call_du_sub(location):
    try:
        result = subprocess.check_output(["du", "-d", "1", location], text=True)
        return result.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return []


def create_dir_dict(du_list):
    dir_dict = {}
    for line in du_list:
        parts = line.split()
        if len(parts) == 2:
            dir_dict[parts[1]] = int(parts[0])
    return dir_dict

