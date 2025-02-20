"""
This module contains function to encode and decode data in base64
"""

def base64encode(msg):
    """Encode a message into a base64 string."""
    i = 0
    base64 = ending = ''
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    # Add padding if string is not dividable by 3
    pad = 3 - (len(msg) % 3)
    if pad != 3:
        msg += "A" * pad
        ending += '=' * pad
    # Iterate though the whole input string
    while i < len(msg):
        word = 0
        # Take 3 characters at a time, convert them to 4 base64 chars
        for j in range(0,3,1):
            # get ASCII code of the next character in line
            nxt = ord(msg[i])
            i += 1
            # Concatenate the three characters together
            word += nxt << 8 * (2-j)
        # Convert the 3 chars to four Base64 chars
        base64 += base64chars[ (word >> 18) & 63 ]
        base64 += base64chars[ (word >> 12) & 63 ]
        base64 += base64chars[ (word >> 6) & 63 ]
        base64 += base64chars[ word & 63 ]
    # Add the actual padding to the end
    if pad != 3:
        base64 = base64[:-pad]
        base64 += ending
    # Print the Base64 encoded result
    return base64


def base64decode(msg):
    """Decode a base64 strint back to a message."""
    i = 0
    decoded = ''
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    # Replace padding with "A" characters so the decoder can process the string,
    # and save the padding length for later
    if msg[-2:] == '==':
        msg = msg[0:-2] + "AA"
        padd = 2
    elif msg[-1:] == '=':
        msg = msg[0:-1] + "A"
        padd = 1
    else:
        padd = 0
    # Take 4 characters at a time
    while i < len(msg):
        data = 0
        for j in range(0,4,1):
            data += base64chars.index(msg[i] ) << (18 - j * 6)
            i += 1
        # Convert the 4 chars back to ASCII
        decoded += chr( (data >> 16 ) & 255 )
        decoded += chr( (data >> 8 ) & 255 )
        decoded += chr( data & 255 )
    # Remove padding
    decoded = decoded[0:len( decoded ) - padd]
    # Print the Base64 encoded result
    return decoded


# Verification

encoded_msg = base64encode('Hello Eggenberg!')
print(encoded_msg)
assert 'SGVsbG8gRWdnZW5iZXJnIU==' == encoded_msg

decoded_msg =base64decode('SGVsbG8gRWdnZW5iZXJnIU==')
print(decoded_msg)
assert 'Hello Eggenberg!' == decoded_msg
