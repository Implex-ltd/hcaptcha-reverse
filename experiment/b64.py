import base64

__n__ = 'YwJlgyomSCMN+/oZdnqz0qxZzKVUx+E1OE+J+5yx+IcjAA=='

class N:
    @staticmethod
    def parse_n(n: str) -> int:
        buff = base64.b64decode(n)

        byte_arr = [b for b in buff]
        bytes_length = len(buff)
        cipher_text = "".join([chr(b) for b in buff])

        print(
            f"""
        \r[n-bytes] {byte_arr[:50]}
        \r[n-len] {len(n)}
        \r[b64-bytes] {bytes_length}
        """
        )

N.parse_n(__n__)

"""
{
    "0": 15,
    "1": 134,
    "2": 168,
    "3": 131,
    "4": 112,
    "5": 27,
    "6": 102,
    "7": 43,
    "8": 73,
    "9": 193,
    "10": 27,
    "11": 100,
    "12": 196,
    "13": 76,
    "14": 21,
    "15": 44,
    "16": 98,
    "17": 185,
    "18": 157,
    "19": 69,
    "20": 222,
    "21": 100,
    "22": 126,
    "23": 245,
    "24": 81,
    "25": 173,
    "26": 22,
    "27": 65,
    "28": 118,
    "29": 73,
    "30": 63,
    "31": 6
}
"""