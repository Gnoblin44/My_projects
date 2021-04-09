# reversing strings bbbyyyy

# a = str(input("Enter: "))
# b = a[::-1]
# print(b)

rev = 'Saif, more like $PATH'


# slicing
def reversed_slicing(s):

    print("\nreversing string or integer")
    return s[::-1]

# print("Reversed string with slicing: %s" % reversed_slicing(rev))   longer and a bit uglier
# print("Reversed string with slicing: ", reversed_slicing(rev))    # actually works


# for loop
def reversed_for_loop(s):
    a1 = ' '
    for i in s:
        a1 = i + a1  # adds the first letter, and then pushes it forward, adds another, so its reversed.#
        print(i)
        """   since a1 is an empty string, a1 becomes 'i' and then adds it back to a1   """
    return a1

# print(f"Reversing with a for loop: {reversed_for_loop(rev)}")


print('\n')
# while loop
def reversed_while_loop(s):
    a1 = ' '
    length = len(s) - 1    # right now it is an integer, but it later is converted to a string #
    while length >= 0:
        a1 += s[length]    # the s'[length]' gets converted to a string. This is really cool, I did not know you could do this #
        """   a1 is an empty string, so it grabs the reverse of 's[length]' which is converted to a string. 
              And so the reverse is placed into a1   """
        # print(a1)
        length -= 1        # removes another from the length of the variable and so the a1 function places it inside of it again #
    return a1

# print("Reversed While Loop: ", reversed_while_loop(rev))


# reversed join and reverse functions
def reversed_join_reverse_str(s):
    a1 = ' '
    temp_lis = list(s)
    temp_lis.reverse()
    return a1.join(temp_lis)

# print(reversed_join_reverse_str(rev))


# reverse with reversed func
def reversed_with_reversed(s):
    a1 = ' '.join(reversed(s))
    return a1

# print(reversed_with_reversed(rev))


# reversed with recursion
def reversed_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reversed_recursion(s[1:]) + (s[0])




def some(x):

    f = 1
    for i in range(1, x+1):
        print(i)
        # print(x)
        f *= i

    return f

print(some(4))