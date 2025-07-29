import random
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs.",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why was the computer cold? It left its Windows open!",
    "Why do Java developers wear glasses? Because they don't see sharp!",
    "Why did the developer go broke? Because he used up all his cache!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the function stop calling itself? Because it had too many stack frames!"
    "Why do python programmers prefer using lists? Because they can append to them!",
    "Why did the web developer leave the restaurant? Because they couldn't find the table!",
    "Why was the developer unhappy at their job? They wanted arrays!",
    "What do the JavaScript say to the Python? 'You complete me!'",
    "Why is it called a 'bug' in programming? Because it makes you feel like you're crawling through the code!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
]

greeting = str(input("Would you like to hear a joke? (yes/no): ").strip().lower())
if greeting == "yes":
    print(random.choice(jokes))
else:
    print("Alright, maybe next time!")