print("Welcome to my computer game!")

playing = input("Do you want to play? ").strip()

if playing.lower() != 'yes':
    quit()

print("Okay lets play 😊")

answer = input("Whats does CPU stands for? ").strip()
if answer.lower() == "central processing unit":
    print("Correct! 🎉")
else: 
    print("Incorrect ❌")

