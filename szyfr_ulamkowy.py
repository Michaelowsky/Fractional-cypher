code = [['A','B','C','D','E'],['F','G','H','I','J'],['K','L','M','N','O'],['P','Q','R','S','T'],['U','V','W','Y','Z']]

while True:
    main = int(input('Type "0" if you want to encrypt message, type "1" if you want to decrypt, type "2" to exit:'))

    if main == 0:
        message = str(input('Type a message you want to encrypt:'))
        list_message = list(message)
        encrypted = ''

        for zero in range(len(list_message)):
            if zero == len(list_message)-1:
                for first in range(len(code)):
                    for second in range(len(code[first])):
                        if list_message[zero] == code[first][second]:
                            encrypted = encrypted + str(second + 1) + '/' + str(first + 1)

            else:
                for first in range(len(code)):
                    for second in range(len(code[first])):
                        if list_message[zero] == code[first][second]:
                            encrypted = encrypted + str(second + 1) + '/' + str(first + 1) + ';'

        print('Your encrypted message is:',encrypted)
        continue

    if main == 1:
        crypted_message = str(input('Write crypted message here in format {number}/{number};{number}/{number};...;{number}/{number} :'))
        list_crypted = list(crypted_message)
        newlist = []
        decrypted = ''

        for sign in list_crypted:
            if sign != '/' and sign != ';':
                newlist.append(sign)

        for one in range(1,len(newlist),2):
            number_one = int(newlist[one])
            number_two = int(newlist[one-1])
            decrypted = decrypted + str(code[number_one-1][number_two-1])

        print('Your decrypted message is:',decrypted)
        continue

    if main == 2:
        exit()

