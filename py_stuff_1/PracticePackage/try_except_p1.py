class TryExceptPractice:

    def __init__(self, cookies, people):
        self.cookies = cookies
        self.people = people

    #@staticmethod
    def party_planner(self):
        leftovers = None
        num_each = None
        # catch ZeroDivisionError
        try:
            num_each = self.cookies // self.people
            leftovers = self.cookies % self.people
        except ZeroDivisionError:
            print("sorry, but what's a party without a person and a cookie?")
        return num_each, leftovers

