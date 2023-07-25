class Converter:

    def __init__(self, answer):
        self.roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        self.int_number = 0
        self.s = list(answer)

    def check_answer(self):

        result = [x for x in self.s if x not in self.roman_numbers]

        if not result:
            return True


    def roman_to_int(self):

        for x in range(0, len(self.s)):

            if self.s[x] == 'I':
                self.int_number += 1

            elif self.s[x] == 'V':
                if x > 0:
                    if self.s[x-1] == 'I':
                        self.int_number += 3
                    else:
                        self.int_number += 5
                else:
                    self.int_number += 5

            elif self.s[x] == 'X':
                if x > 0:
                    if self.s[x-1] == 'I':
                        self.int_number += 8
                    else:
                        self.int_number += 10
                else:
                    self.int_number += 10

            elif self.s[x] == 'L':
                if x > 0:
                    if self.s[x-1] == 'X':
                        self.int_number += 30
                    else:
                        self.int_number += 50
                else:
                    self.int_number += 50

            elif self.s[x] == 'C':
                if x > 0:
                    if self.s[x - 1] == 'X':
                        self.int_number += 80
                    else:
                        self.int_number += 100
                else:
                    self.int_number += 100

            elif self.s[x] == 'D':
                if x > 0:
                    if self.s[x-1] == 'C':
                        self.int_number += 300
                    else:
                        self.int_number += 500
                else:
                    self.int_number += 500

            elif self.s[x] == 'M':
                if x > 0:
                    if self.s[x-1] == 'C':
                        self.int_number += 800
                    else:
                        self.int_number += 1000
                else:
                    self.int_number += 1000
