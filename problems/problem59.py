"""Problem 59 - Project Euler

XOR decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with
a given value, taken from a secret key. The advantage with the XOR function is that using the same
encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made
up of random bytes. The user would keep the encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

Algorithm
 * find three lower case characters that produce text that has a lot of [A-Za-z ] characters - 4 secs, good enough
    * most time is spent in _crypt even though it is called only 15600 times (XOR is slow?)
 * i'm sure it would be faster to do character/term frequency but this was easy
"""
import itertools as it


class Problem59(object):
    @staticmethod
    def solve():
        def _crypt(cipher, key):
            return (p[0] ^ p[1] for p in zip(cipher, it.cycle(key)))

        _good_chars = set(it.chain(range(ord('A'), ord('A')+1), range(ord('a'), ord('z')+1), range(ord('0'), ord('9')+1), (ord(' '), ord('.'))))
        def _fraction_good(ascii):
            return sum(1 for v in ascii if v in _good_chars) / len(ascii)

        best = 0, None, None
        cipher = list(Problem59.read_cipher())
        for key in it.permutations(range(ord('a'), ord('z')+1), 3):
            ascii = list(_crypt(cipher, key))
            if any(a < 32 or a > 125 for a in ascii): continue  # quick reject unprintables
            fraction = _fraction_good(ascii)
            if fraction > best[0]:
                best = fraction, sum(ascii), key

        # def _as_text(ascii):
        #     return ''.join(chr(a) for a in ascii)
        # print(_as_text(best[2]))
        # print(_as_text(_crypt(cipher, best[2])))
        return best[1]

    @staticmethod
    def read_cipher():
        with open('../resources/p059_cipher.txt') as file:
            return (int(s) for s in file.read().split(','))

    @staticmethod
    def get_tests():
        return [(None, 107359)]


if __name__ == '__main__':
    print("The answer is", Problem59.solve())
