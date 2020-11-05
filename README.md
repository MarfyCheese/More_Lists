The attached repository has three functions you need to implement. Each one of them requires the use of a list comprehension. main has already been implemented, you just need to complete these functions. You should not use a for loop anywhere in this assignment.

1: Implement 'sum_of_odd_nums' to return the sum of the first n odd numbers. For example, the first 3 odd numbers are 1, 3, and 5, and their sum is 9. Do this by using a list comprehension to generate a list of the first n odd numbers, and then using the sum function to sum the list.

2: Implement a Caesar cipher in the function 'caesar_cipher'. This function takes a string and a number, which will serve as a key. For each character in the string, convert it to a number using the 'ord' function, then add 'key' to it. This will give you a list of numbers. To convert this back to a string, use the 'bytes' function to convert it to a bytestring, then use the 'decode' method of the bytestring to covert the bytes to ascii characters. (This part will be tricky if you've never worked with these functions. Don't hesitate to ask me for help.) I've included an encoded message along with the key needed to decode it. Implement the function to decode the message.

3: Implement 'fizzbuzz', a classic job interview question, with a list comprehension. This function should return a list of numbers from 1 to n, except if a number is divisible by 3 it is replaced by the string 'Fizz!', if it is divisible by 5 it should be replaced by the string 'Buzz!', and if it is divisible by both 3 and 5 it should be replaced by the string 'Fizzbuzz!'. For example, fizzbuzz(6) should return [1, 2, 'Fizz!', 4, 'Buzz!', 6]. To do this, make a helper function which acts on a number, returning the proper string if appropriate and returning the number otherwise. Then, use this function in a list comprehension to generate the list.

As always, begin by forking my repository and then either clone it to your machine or open it on repl.it. Submit your repository to complete the assignment.