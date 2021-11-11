import itertools
import time

number = int(input("How many numbers will you enter?"))
words = []
attemps = 0

for i in range(number) :
    word = input("enter the word")
    words.append(word)

file = open("password.txt","a")

start_range = 2
end_range = 4

start_time = time.time()
for password_length in range(start_range,end_range):
    for guess in itertools.product(words, repeat=password_length):
        attemps += 1
        guess = ''.join(guess)
        file.write(guess)
        file.write("\n")

        print(guess, attemps)

file.close()


end_time = time.time()

print(f"password generation took {end_time-start_time}")
print(f"{attemps} passwords created")