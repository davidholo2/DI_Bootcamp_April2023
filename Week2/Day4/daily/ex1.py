matrix = ['7i3', 'Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', '^r!']
message = []

for i in range(len(matrix[0])):
    alpha_chars = ''
    for j in range(len(matrix)):
        if matrix[j][i].isalpha():
            alpha_chars += matrix[j][i]
    message.append(alpha_chars.replace('*', ' '))

decrypted_message = ''.join(message)

print(decrypted_message)
