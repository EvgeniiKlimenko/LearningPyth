
fruits = ["cherry", "apple", "melon", "watermelon", "orange"]
print(fruits)
print(len(fruits))
print("melon" in fruits)  # returns bool
fruits[0], fruits[4] = fruits[4], fruits[0]  # swap elements in list
print(fruits)

my_lest1 = [1, 2, 5]
my_lest2 = [1, 5, 5]
print(my_lest1 == my_lest2)  # comparing what's inside

print(bool([]))  # bool from empty list - FALSE
print(bool([1, 5, 2.5]))  # bool from NOT empty list - TRUE

word = "hello"
chars = list(word)  # every char in word will be a separate element of a list
print(chars)

numbersList = [5, 12, 1, 165, 87, 86, 11]
numbersList.sort()
print(numbersList)
numbersList.sort(reverse=True)  # descending sorting
print(numbersList)
print(max(numbersList))  # find max element in list. Also min() and sum()
print(numbersList[::-1])  # reverse the list

frase = "Hello dear world of programming"
wordsList = frase.split(" ")  # create list of words by delimiter
print(wordsList)
joined_string = " ".join(wordsList)  # create a single string from list of words by delimiter
print(joined_string)

# slices
numbers_list = [5, 12, 1, 165, 87, 86, 11]
print(numbers_list[0:3])  # 0 include, 3 not include. [3:len()],
print(numbers_list[0:len(numbers_list):2])  # every 2nd element from 0 to len(list)

# ranges
range_object = range(10)
range_object_two = range(1, 20, 2)  # from 1 to 20 with step 2
numbers_range = list(range_object)  # create a list 1-10 from range object
