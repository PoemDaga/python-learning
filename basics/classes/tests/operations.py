my_str = "Hello World"
print(my_str[3])  # l

n = 15

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)

my_str = "Hello MoTO"

final_str = ""
for word in my_str.split():
    final_str = word.swapcase() + " " + final_str

print(final_str)



# a function to reverse order of words in a string and swap case
def reverse_and_swap_case(my_str):
    # split the string into words
    words = my_str.split(" ")
    # reverse the order of words
    words = words[::-1]
    # join the words
    words = " ".join(words)
    # swap case
    words = words.swapcase()
    return words


print(reverse_and_swap_case("aWESOME is cODING"))

