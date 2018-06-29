from PracticePackage.bert_script_9 import BertEnumZip
#from PracticePackage.eval_demo_2 import *
import try_except_p1
import reading_files
import subprocess
import SimpleParser

from PracticePackage.eval_demo_2 import secret_function


def dowork1():
    BertEnumZip.exe()

def tryexceptp():
    # The main code block is below; do not edit this
    lets_party = 'y'

    while lets_party == 'y':

        cookies = int(input("How many cookies are you baking? "))
        people = int(input("How many people are attending? "))
        tep = try_except_p1.TryExceptPractice(cookies, people)
        cookies_each, leftovers = tep.party_planner()

        if cookies_each:  # if cookies_each is not None
            message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
            print(message.format(people, cookies_each, leftovers))

        lets_party = input("\nWould you like to party more? (y or n) ")

def tryevaldemo(self):
    secret_function()

# Main
# dowork1()
#tryexceptp()
#subprocess.call("reading_files.py", shell=True)
#subprocess.call("writing_files.py", shell=True)
#subprocess.call("appending_to_files.py", shell=True)
#subprocess.call("autoclose_file.py", shell=True)
#subprocess.call("read_incremental.py", shell=True)

# looking into using sys.argv[1]
# https://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-args
subprocess.call("SimpleParser.py", 3, shell=True)


