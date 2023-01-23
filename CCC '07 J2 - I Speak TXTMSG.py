text_dict = {"CU": "see you", ":-)": "I'm happy", ":-(": "I'm unhappy", ";-)": "wink", ":-P": "stick out my tongue",
             "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because",
             "TY": "thank-you", "YW": "you're welcome", "TTYL": "talk to you later"}

word = input()
while word != "TTYL":
    if word in text_dict:
        print(text_dict.get(word))
    word = input()
    if word not in text_dict:
        print(word)

print("talk to you later")