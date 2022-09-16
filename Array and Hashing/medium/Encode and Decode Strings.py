class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""
        for s in strs:
            for c in s:  # c is char in string
                encoded += (str(chr(ord(c)+2)))
            encoded += ("#")
        return encoded


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, string):
        decoded = []
        curr = ""
        for s in string:
            for c in s:  # c is char in string
                if c == "#":
                    decoded.append(curr)
                    curr = ""
                    continue

                curr += str(chr(ord(c)-2))
        return decoded




# FASTER VERSION

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += s
            encoded += "`"
        return encoded[0:-1]


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, string):

        return string.split(sep="`")

# REAL MAN VERSION where the seperator info is included in the string

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
        # o(n) solution
        '''return ''.join(
        f'{len(string)}#{string}'
        for string in strs)
        '''

    def decode(self, string):
        num = ""
        ans = []
        i = 0  # pointer
        while i < len(string)-1:
            if string[i] in "1234567890":
                num += string[i]
            else:  # when the char is #
                ans.append(string[i+1:i+int(num)+1])
                i += int(num)
                num = ''
            i+=1
        return ans

    input = ["lint","code","love","you"]
    print(encode(2,input))
    encoded = encode(2,input)
    print(decode(2, encoded))

