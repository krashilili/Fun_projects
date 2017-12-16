# Puzzle #1
# Find the smallest palindromic number in decimal that is larger than 10,
# meanwhile, the number is also palindromic in binary and octal.

# Palindromic number: is a number that remains the same when its digits are
# reversed, e.i. "16461", "12321", and "1001001".

import time


def find_palindromic_num(num_in_dec):
    t1 = time.time()
    while(True):
        if num_in_dec > 10:
            # print("%s"%(num_in_dec))
            ns_dec = str(num_in_dec)
            if ns_dec == ns_dec[::-1]: # reversed
                # print('This number in decimal is palindromic.')
                # convert to binary
                num_in_bin = bin(num_in_dec)
                ns_bin = str(num_in_bin)[2:]
                if ns_bin == ns_bin[::-1]:

                    # print('This number in binary is palindromic.')

                    # conver to octal
                    num_in_oct = oct(num_in_dec)
                    ns_oct = str(num_in_oct)[2:]
                    if ns_oct == ns_oct[::-1]:
                        print('This number in octal is palindromic.')
                        print('Find the number!')
                        print("decimal: {}, binary: {}, octal: {}".format(num_in_dec, bin(num_in_dec), oct(num_in_dec)))
                        dt = time.time() - t1
                        print("Time cost: {}s".format(dt))
                        return True

                    else:
                        # print('This number in octal is palindromic.')
                        num_in_dec += 1
                        # find_palindromic_num(num_in_dec)

                else:
                    # print('This number in binary is not palindromic')
                    num_in_dec += 1
                    # find_palindromic_num(num_in_dec)

            else:
                # print('This number in decimal is not palindromic.')
                num_in_dec += 1
                # find_palindromic_num(num_in_dec)
        else:
            print("The decimal number should be larger than 10.")


def a_better_solution(num_in_dec):
    # Only considering the odd numbers because if the binary number
    # is palindromic, it has to starts with '1' and ends with '1'.
    t1 = time.time()
    while(True):
        # print(num_in_dec)
        # ns_in_dec = str(num_in_dec)
        # ns_in_oct = str(oct(num_in_dec))[2:]
        # ns_in_bin = str(bin(num_in_dec))
        if str(num_in_dec)==str(num_in_dec)[::-1] \
                and str(bin(num_in_dec))[2:] == str(bin(num_in_dec))[2:][::-1]\
                and str(oct(num_in_dec))[2:] == str(oct(num_in_dec))[2:][::-1]:
            print('This number in octal is palindromic.')
            print('Find the number!')
            print("decimal: {}, binary: {}, octal: {}".format(num_in_dec, bin(num_in_dec), oct(num_in_dec)))
            dt = time.time() - t1
            print("Time cost: {}s".format(dt))
            return True
        else:
            num_in_dec += 2


if __name__ == '__main__':
    find_palindromic_num(11)
    # a_better_solution(11)