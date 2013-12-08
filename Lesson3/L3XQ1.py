# Investigating adding and appending to lists

# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5]
list2.append(5)

# to check, you can print them out using the print statements below.

print list1
print list2
print '***'

# What is the difference between these two pieces of code?
# Append takes the original list object and adds the additional list item on the end
# Concatenating the list creates a new object with the new item added on the end
# but it doesn't maodify the original list inputs


def proc(mylist):
    mylist = mylist + [6]

def proc2(mylist):
    mylist.append(6)

# Can you explain the results given by the four print statements below? Remove
# the hashes # and run the code to check.
# proc method concatenates so it creates a new object, mylist (on left), but
# when that's printed out, it still prints the original object mylist (on right)
# basically mylist is reference is passed in proc2 whereas mylist is immutable so
# proc makes a new list?

print list1
proc(list1)
print list1

print list2
proc2(list2)
print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4]
list3 += [5]

# Does this behave like list1 = list1 + [5] or list2.append(5)? Write a
# procedure, proc3 similar to proc and proc2, but for +=. When you've done
# that check your conclusion using the print-procedure call-print code as
# above.

def proc3(mylist):
    mylist += [5]
    
# What happens when you try:

print '***'
list1 = list1 + [7,8,9]
print list1
list2.append([7,8,9])
print list2
list3 += [7,8,9]
print list3

# When you've understood the difference between the three methods,
# write a procedure list_test which takes three lists as inputs. You should
# mutate the first input list to include 'a' as the last entry, mutate the
# second to include the entries 'a', 'b', 'c' and finally the last list should
# not be mutated but a copy should be returned with the additional entry 'w'.

def list_test(l1,l2,l3):
    l1.append('a')
    l2 += ['a','b','c']
    return l3.append('w')


first_input = [1,2,3]
second_input = [4,5,6]
third_input = [7,8,9]

print list_test(first_input, second_input, third_input)
#>>> [7,8,9,'w']
print first_input
#>>> [1,2,3,'a']
print second_input
#>>> [4,5,6,'a','b','c']
print third_input
#>>> [7,8,9]

