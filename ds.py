secret_word = "giraffe"

guess = ""

i = 1
while guess != secret_word:
    if i <= 1:
        i += 1
        guess = input("guess the secret work \n Hint: Its an animal with a long neck \n Enter:")
    elif i > 1:
        i += 1
        guess = input("WRONG \n guess the secret work \n Hint: Its an animal with a long neck \n Enter:")
print("You win!")
