from PracticePackage.bert_script_9 import BertEnumZip
from PracticePackage.eval_demo_2 import *
from PracticePackage.try_except_p1 import TryExceptPractice


class Tabletop(object):
    def dowork1(self):
        BertEnumZip.exe()

    def tryexceptp(self):
        # The main code block is below; do not edit this
        lets_party = 'y'

        while lets_party == 'y':

            cookies = int(input("How many cookies are you baking? "))
            people = int(input("How many people are attending? "))

            cookies_each, leftovers = TryExceptPractice.party_planner(cookies, people)

            if cookies_each:  # if cookies_each is not None
                message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
                print(message.format(people, cookies_each, leftovers))

            lets_party = input("\nWould you like to party more? (y or n) ")

    def tryevaldemo(self):
        secret_function()


def main():
    t = Tabletop()
    #  t.dowork1()
    t.tryexceptp()


if __name__ == "__main__":
    main()

