# FIND AND REPLACE
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

words = "It's thanksgiving day It's my birthday, too!"
x = "day"
print words.find(x)
print words.replace("day", "month")

# MIN AND MAX
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

my_list = [1,2,3,4,5]
print min(my_list)
print max(my_list)

# FIRST AND LAST
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

my_list = ["hello",1,2,3,4,"world"]
print my_list.pop(0)
print my_list.pop()

# NEW LIST
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

list = [19,2,54,-2,7,12,98,32,10,-3,6]
list.sort()
print list
firstHalf = list[0:5]
print firstHalf
secondHalf = list[5:11]
print secondHalf
newList = secondHalf.insert(0,firstHalf)
print newList
