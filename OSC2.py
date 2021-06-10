from random import randrange as rr

class marx:

    def __init__(self, byte = 126):
        if byte < 126:
            raise Exception("byte can't be less than 126")
            return
        self.__byte = byte
        self.__chardict = {"basic":self.__getCharacters(end = self.__byte)}
        self.__chardict.update({"greek":self.__getCharacters(880,1023)})
        self.__chardict.update({"cyrillic":self.__getCharacters(1024,1327)})
        self.__chardict.update({"armenian":self.__getCharacters(1328,1423)})
        self.__chardict.update({"hebrew":self.__getCharacters(1424,1524)})
        self.__chardict.update({"arabic":self.__getCharacters(1536,2303)})
        self.__chardict.update({"thai":self.__getCharacters(3583,3675)})
        self.__chardict.update({"tagalog":self.__getCharacters(5888,5908)})
        self.__chardict.update({"japthin":self.__getCharacters(12353,12543)})
        self.__chardict.update({"japthick":self.__getCharacters(12549,12589)})
        self.__chardict.update({"hangul":self.__getCharacters(12593,12686)})
        self.__chardict.update({"cjk":self.__getCharacters(19968,22016)})#40959
        self.__chardict.update({"runic":self.__getCharacters(5792,5872)})
        self.__chardict.update({"braille":self.__getCharacters(10240,10495)})
        self.__additional = self.__chardict["runic"] + self.__chardict["braille"] #+ self.__chardict["greek"]#+ self.__chardict["greek"]
        self.__characters = self.__chardict["basic"] + self.__additional

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
        del self.__chardict
        return keys

    def __refragment(self, keys):
        keys.reverse()
        new_keys = keys
        del keys
        return new_keys

    def __processQuery(self, message, keys, encrypt):
        for code in keys:
            #print(code)
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
            print(temp)
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
            if temp in bank or temp == ' ' or temp == '\n' or (temp in self.__chardict["basic"]):
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

    banned = []#[3643, 3644, 3645, 3646]

    def __getCharacters(self, start = 0, end = 126):
        chars = []
        try:
            while start <= end: #126 default
                chars.append(chr(start))
                start+=1
        except:
            pass
        chars.reverse()
        return chars  
    
    '''
        0-126 standard keyboard
        0-191 more special characters
        0-687 Latin characters and extras
        688-767 Modifiers
        768-879 Combining
        
    '''

key = marx().generate()
#text = str(input("Text: "))
text = "Hello, I am Mar.zZ"
#text = "abcdefghijklmnopqrstuvwxyz###ABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp = marx().encrypt(text, key)
print("Encrypt:", temp)
#print("Decrypt:", marx().decrypt(temp, key))
#print("Key:", key)
