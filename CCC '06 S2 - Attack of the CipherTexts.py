plaintext = input()
ciphertext = input()
decode = input()
code = {}

for i in range(len(ciphertext)):
    code[ciphertext[i]] = plaintext[i]

normal = ""
for i in range(len(decode)):
    if decode[i] in code:
        normal += code[decode[i]]
    else:
        normal += "."
print(normal)