def sum_of_odd_nums(n):
    l = list(range(1,n*2))
    new_l = [i for i in l if i%2==1]
    return sum(new_l)
def caesar_cipher(message, key):
    ordMessage = [ord(i) + key for i in message]
    bytesMessage = bytes(ordMessage)
    return bytesMessage.decode("ascii")
def fizzbuzzHelp(n):
  if n%3 == 0 and n%5 == 0:
    return "Fizzbuzz!"
  elif n%3 == 0:
    return "Fizz!"
  elif n%5 == 0:
    return "Buzz!"
  else:
    return n
def fizzbuzz(n):
    fizzList = [fizzbuzzHelp(i) for i in range(1,n+1)]
    return fizzList

def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(1,11):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "Frpsxwhu#Vflhqfh#lv#qr#pruh#derxw#frpsxwhuv#wkdq#dvwurqrp|#lv#derxw#whohvfrshv1"
    print(caesar_cipher(ciphertext, -3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()