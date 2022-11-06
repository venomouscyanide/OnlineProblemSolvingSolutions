# https://leetcode.com/problems/encode-and-decode-strings/


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        self.delim = "$%$" * len(strs)
        new_str = ""
        for str in strs:
            new_str += f"{self.delim}{str}"
        return new_str

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        return s.split(self.delim)[1:]


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    strs = ["Hello", "World"]
    codec = Codec()
    print(codec.decode(codec.encode(strs)))

    strs = ["Hey ", "", "", ""]
    codec = Codec()
    print(codec.decode(codec.encode(strs)))
