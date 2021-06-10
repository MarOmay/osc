from random import randrange as rr

class marx:

    '''
        encrypt(message, key) - returns encrypted message
        decrypt(message, key) - returns decrypted message
        generate() - returns a random combination of characters
    '''

    def __init__(self):
        self.__characters = self.__getCharacters()

    def encrypt(self, message, key):
        return self.__processQuery(message, self.__defragment(key), True)

    def decrypt(self, message, key,):
        return self.__processQuery(message, self.__refragment(self.__defragment(key)), False)

    def __defragment(self, key):
        initial = 0
        final = 4
        keys = []
        lap = 64
        while lap > 0:
            keys.append(key[initial:final])
            initial = final
            final+=4
            lap-=1
        del initial
        del final
        del lap
        return keys

    def __refragment(self, keys):
        keys.reverse()
        new_keys = keys
        del keys
        return new_keys

    def __processQuery(self, message, keys, encrypt):
        for code in keys:
            first_dict = {}
            new_chars = []
            for char in code:
                new_chars.append(char)
            for i in self.__characters:
                if i in new_chars:
                    continue
                else:
                    new_chars.append(i)
            ctr = 0
            for i in self.__characters:
                if encrypt:
                    second_dict = {i:new_chars[ctr]}
                else:
                    second_dict = {new_chars[ctr]:i}    
                first_dict.update(second_dict)
                ctr+=1
            temp = ""
            for letter in message:
                if letter in new_chars:
                    temp = temp + first_dict[letter]
                else:
                    temp = temp + letter
            message = temp
            del temp
            del first_dict
            del second_dict
            del new_chars
            del ctr
        return message

    def generate(self):
        key = ""
        ctr = 256
        ctl = 4
        bank = []
        temp = ""
        while ctr > 0:
            if ctl == 0:
                bank.clear()
                ctl = 4
            temp = self.__characters[rr(0,len(self.__characters)-1)]
            if temp in bank or temp == ' ' or temp == '\n':
                continue
            else:
                key = key + temp
                bank.append(temp)
                ctl-=1
                ctr-=1
        del ctr
        del ctl
        del bank
        del temp
        return key

    def __getCharacters(self):
        i = 0
        chars = []
        try:
            while i <= 1024: #126 default
                chars.append(chr(i))
                i+=1
        except:
            pass
        return chars

key = marx().generate()
text = str(input("Text: "))#"Hello, I am Mar."
temp = marx().encrypt(text, key)
print("Encrypt: ", temp)
print("Decrypt: ", marx().decrypt(temp, key))
#print("Key: ", key)
