class PhonePlan:
    def __init__(self, mins=0, msgs=0):
        self.num_mins = mins
        self.num_messages = msgs

    def print_plan(self):
        print('Mins:', self.num_mins, end=' ')
        print('Messages:', self.num_messages)

my_plan = PhonePlan(200, 300)
dads_plan = PhonePlan()

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()