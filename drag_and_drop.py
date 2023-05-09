#|/usr/bin/python

"""
Created on Wed Jan  4 11:41:36 2023

@author: khadim and Ahmad 

https://github.com/enasequence/webin-cli/releases

"""

import argparse, os,sys
from modules.DragAndDropSubmission import DDSubmission

def get_args():
    parser = argparse.ArgumentParser(prog='download_data.py', formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="""
        + ============================================================ +
        |  European Nucleotide Archive (ENA): drag and drop submission |
        |                                                              |
        + ============================================================ +
        """)
    parser.add_argument('-u', '--user', help='Your OPS$USER', type=str, required=True)
    parser.add_argument('-p', '--opspasswd', help='Enter you OPS password', type=str, required=True)
    parser.add_argument('-sp', '--suppasswd', help='Enter the super user password', type=str, required=True)
    parser.add_argument('-w', '--webin_accout', help='Webin-XXXXXX', type=str, required=True)
    parser.add_argument('-t', '--test_sub', help='Do you use ENA test server for submission? [yes/no]', choices=['YES','NO'], required=True)
    parser.add_argument('-f', '--file', help='path for the metadata spreadsheet (On excel file format)', type=str, required=True)
    parser.add_argument('-a', '--action', help='Specify the type of action needed ( ADD )', choices=['ADD'], required=True)
    
    args = parser.parse_args()
    return args
args = get_args()
user = args.user
opspasswd = args.opspasswd
suppasswd = args.suppasswd
webin_accout = args.webin_accout
test_sub = args.test_sub
file = args.file
action = args.action

if test_sub.upper() == 'YES':
    t = '-t'
elif test_sub.upper()=='NO': 
    t = ' '
if action.upper() == 'ADD':
    action = 'ADD'

submit = DDSubmission.submission(user, opspasswd, suppasswd, webin_accout, t, file,action )




