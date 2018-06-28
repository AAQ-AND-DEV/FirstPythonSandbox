""" bert_script_9.py
"""


class BertEnumZip(object):

    @classmethod
    def exe(self):
        names = input("enter names, sep=','").split(',')  # get and process input for a list of names
        assignments = input("enter num, sep=','").split(',')  # get and process input for a list
        # of the number of assignments
        grades = input("enter grades, sep=','").split(',')  # get and process input for a list of grades
        bumped = [int(x)+47 for x in grades]
        # message string to be used for each student
        # HINT: use .format() with this string in your for loop
        message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
        submit before you can graduate. You're current grade is {} and can increase \
        to {} if you submit all assignments before the due date.\n\n"
        # write a for loop that iterates through each set of names, assigns, and grades to print each student's message
        objs = zip(names, assignments, grades, bumped)
        for i, (name, assignment, grade, bump) in enumerate(objs):
            print(message.format(name, assignment, grade, bump))