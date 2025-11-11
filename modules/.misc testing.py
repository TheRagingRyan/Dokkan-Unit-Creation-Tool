def Create_JSON_Output(data):
    import ast
    source_text = data
    compiled_text = ''
    text = ''
    dictionary = {}
    list_text = []
    if '&' in data and '|' in data and '(' not in data:
        print('1st conditional')
        num = ''
        for char in data:
            if char.isdigit():
                num += char
            else:
                if char == '|':
                    list_text.append(str(num) + ']')
                    num = ''
                else:
                    list_text.append('[' + str(num))
                    num = ''
        list_text.append(str(num) + ']')
        
        # list_text = eval(list_text)

        list_text = str(list_text)
        # list_text = list_text[:-1]
        # list_text = list_text[1:]
        list_text = list_text.replace('\'', '')
        list_text = eval(list_text)
        for i in range(len(list_text)):
            list_text[i] = str(list_text[i])[1:]
            list_text[i] = '[\"&\", ' + str(list_text[i])
        # for i in range(len(list_text)):
            # if 
        # print(str(list_text[0]))
        
        # print(list_text)
        # print(str(list_text)[1:])
        text = '[\"|\", ' + str(list_text)[1:].replace('\'', '')
        
        compiled_text = text
        
    elif '&' in data and '|' in data and '(' in data:
        print('2nd conditional')
        if data[0] == '(':
            data = data.replace('(', '[').replace(')', ']').replace('|', ',').replace('&', ',')
            data = '[' + data + ']'
            data = eval(data)

            test_list = []
            list_text = ['\"|\" ']
            for i in range(len(data)):
                test_list.append(str(data[i]).replace('[', ', '))
            
            # print(test_list.)

            for i in range(len(data)):
                text += '[\"&\"' + test_list[i] + ', '

            
            text = '[\"|\", ' + text
            text = text[:-2] + ']'
            
            # print(text.replace(' , ', ' [\"|\", '))
            if ' , ' in text:
                compiled_text = text.replace(' , ', ' [\"|\", ')
            else:
                compiled_text = text
            
        else:
            
            data = data.replace('(', '[').replace(')', ']').replace('|', ',')
            dictionary = {}
            
            num = ''
            x = 0
            for char in data:
                x += 1
                num += char
                if char == '&':
                    data = data[x:]
                    break
                
            and_symbol = num[-1]
            
            text = '[\"'
        #             first_operand = 'and'
        #             break
                
        #         elif char == '|':
        #             first_operand = 'or'
        #             break
                
        #     if first_operand == 'and':
        #         pass
                
                # if char.isdigit():
                #     num += char
                # else:
                #     if char is '|':
                #         dictionary = {}
                #     num = ''
        
        # print(data)
    
    elif '&' in data and '|' not in data:
        data = data.replace('&', ', ')
        data = '[\"&\", ' + data + ']'
        compiled_text = data
    
        
        
    elif '|' in data and '&' not in data:
        data = data.replace('|', ', ')
        data = '[\"|\", ' + data + ']'
        compiled_text = data
    
        
    compiled_text = '{' + '\"source\": ' + '\"' + source_text + '\"' + ', ' + '\"compiled\": ' + compiled_text + '}'
    return compiled_text
            



# Working
text = "1937&1938|1939&1940"
# text = "(1937&1938)|(1939&1940)|(5555&5523)"
# text = "(385&(386|387))|(388&9)"


# text = "494&(479|480|481)"
# text = "4&(819|820)|6&(222|333)"
#  Expected Outcome ["&", 4, ["|", 819, 820]]


# Expected Output ["|", ["&", 1937, 1938], ["&", 1939, 1940]]


# Expected output ["|", ["&", 385, ["|", 386, 387]], ["&", 388, 9]]
# compiled = Create_JSON_Output(text)
# print(compiled)



#########################################################################################################################################################################################################################
# from pypresence import Presence
# import time

# # Initialize the Presence instance
# RPC = Presence(774666488690769930)

# # Connect to Discord
# RPC.connect()

# # Set the Rich Presence information
# RPC.update(
#     state=None,
#     details="Brainstorming",
#     large_image="zamasu_and_vegito",
#     small_image="zamasu",
#     start=time.time(),
#     buttons=[{"label": "Test Button", "url": "https://example.com"}]
#     # https://discord.gg/EWTyTnPhn7
# )

# # Main loop to keep the connection alive (you can modify this as needed)
# while True:
#     time.sleep(15)

# import sqlite3
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad

# # Connect to the SQLite database
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# # Retrieve the encrypted data from the database
# cursor.execute('SELECT name FROM cards')
# encrypted_data = cursor.fetchone()[0]

# # Decrypt the data (AES decryption)
# key = b'2db857e837e0a81706e86ea66e2d1633'  # Replace with your encryption key
# cipher = AES.new(key, AES.MODE_ECB)
# decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

# # Now, `decrypted_data` contains the decrypted information

# # Close the database connection when done
# conn.close()

