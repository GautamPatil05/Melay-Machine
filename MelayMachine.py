class MealyMachine:
    def __init__(self):
        self.state = 'start'
        self.output = ''

    def transition(self, input):
        if self.state == 'start':
            if input == '0':
                self.state = 'q0'
            elif input == '1':
                self.state = 'q1'
            self.output = ''
        elif self.state == 'q0':
            if input == '0':
                self.state = 'q0'
            elif input == '1':
                self.state = 'q1'
            self.output = ''
        elif self.state == 'q1':
            if input == '0':
                self.state = 'q2'
            elif input == '1':
                self.state = 'q1'
            self.output = ''
        elif self.state == 'q2':
            if input == '0':
                self.state = 'q0'
            elif input == '1':
                self.state = 'q3'
            self.output = ''
        elif self.state == 'q3':
            if input == '0':
                self.state = 'q2'
            elif input == '1':
                self.state = 'q1'
            self.output = ''

    def get_output(self):
        if self.state == 'q3':
            return 'A'
        elif self.state == 'q2':
            return 'B'
        else:
            return 'C'

# Giving input
input_sequence = '101010101' # output: 'A'
# input_sequence = '101010110' # output: 'B'
# input_sequence = '101010111'   # output: 'C'
# input_sequence = input("Enter the String: );
mealy_machine = MealyMachine()
for input_char in input_sequence:
    mealy_machine.transition(input_char)

final_output = mealy_machine.get_output()
print(final_output)  

# Works