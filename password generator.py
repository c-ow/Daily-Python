import random, string
from string import punctuation

alphabet = list(string.ascii_lowercase)
special = list(punctuation)

pass_len = input("How many characters would you like your password to be? ")
password = []

if pass_len.isnumeric():
    spec = input('Add special characters? yes or no\n')
    for i in range(int(pass_len)):
        rand_letter = alphabet[random.randint(0,25)]
        choices = [random.randint(0,9), rand_letter, rand_letter.upper()]
        if spec.lower() == 'yes':
            rand_spec = punctuation[random.randint(0, len(punctuation)-1)]
            choices.append(rand_spec)
        rand_order = random.choice(choices)
        password.append(rand_order)
    password = ''.join(str(x) for x in password)
    print('Your generated pasword is: %s' % (password))
else:
    print('Could not read input.')