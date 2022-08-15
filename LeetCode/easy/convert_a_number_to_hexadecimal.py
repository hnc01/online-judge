class Solution:
    def toHex(self, num: int) -> str:
        hexRepresentation = ""

        characters = "0123456789abcdef"

        # we have 32 bits but we need to treat each 4 bits separately
        # 32 / 4 = 8 iterations
        for i in range(0, 8):
            # we need to isolate the last 4 bits
            # to do that, we & with 15 which is 0000 ... 0000 1111
            last4Bits = num & 15

            # now last4Bits will act like our index in characters
            hexRepresentation = characters[last4Bits] + hexRepresentation

            # now we need to get rid of the last 4 bits
            num >>= 4

            if num == 0:
                break

        return hexRepresentation