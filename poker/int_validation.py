import string
def get_int(prompt):
    valid = False
    while not valid:
        x = raw_input(prompt)
        if x in ["","-"]:
            continue
        elif x == '0':
            return 0
        neg = False
        if x[0] == '-':
            neg = True
            x = x.lstrip('-')
        x = x.lstrip('0')
        for char in x:
            if char not in string.digits:
                break
        else:
            valid = True
    if neg:
        return -int(x)
    else:
         return int(x)

if __name__ == '__main__':
    while True:
        num = get_int("Enter an integer: ")
        print num
