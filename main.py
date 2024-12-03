import requests

#random word generater url
url = "https://random-word-api.vercel.app/api?words=1&length="
length = int(input("Enter your desired length of word(max is 9 and min is 3)\n>>> "))

if length > 9 or length < 3:
    raise ValueError("Enter a valid length")


word = ""
guess=""
tries = 10


try:
    req = requests.get(url+str(length))
    if req.status_code == 200:
        content = req.json()
        word = content[0]
    else:
        exit("Something bad happened")
except Exception as e:
    print(e)

wordLst = list(word)

state = ["_"*1 for i in range(len(word))]


while tries > 0:
    userInput = input("Enter a guess.\n>>> ").lower()

    if userInput in wordLst:
        tries -= 1
        print("Correct guess.")
        if wordLst.count(userInput) == 1:
            gIndex = wordLst.index(userInput)
            state[gIndex] = userInput
            stateStr = "".join(state)
            print(stateStr)
            print(f"Remaining tries: {tries}")
            if state == wordLst:
                print(f"You guessed the word correctly in {tries} tries") if tries > 1 else print(f"You guessed the word correctly in {tries} try")
                break

        elif wordLst.count(userInput) > 1:
            gIndex = wordLst.index(userInput)
            gIndex1 = wordLst.index(userInput, wordLst.index(userInput)+1)
            state[gIndex] = userInput
            state[gIndex1] = userInput
            stateStr = "".join(state)
            print(stateStr)
    
    if userInput not in wordLst:
        tries -= 1
        stateStr = "".join(state)
        print(f"Incorrect guess. You now have {tries} tries") if tries>1 else print(f"Incorrect guess. You now have {tries} try")
        print(stateStr)
else:
    print(f"Oops! You ran out of tries. The word was {word}")


#to do:
#   make the code readable
