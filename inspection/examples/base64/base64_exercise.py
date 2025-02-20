import sys

def base64encode(s):
    i = 0
    base64 = ending = ''
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    # Add padding if string is not dividable by 3
    pad = 3 - (len(s) % 3)
    if pad != 3:
        s += "A" * pad
        ending += '=' * pad
    # Iterate though the whole input string
    while i < len(s):
        b = 0
        # Take 3 characters at a time, convert them to 4 base64 chars
        for j in range(0,3,1):
            # get ASCII code of the next character in line
            n = ord(s[i])
            i += 1
            # Concatenate the three characters together
            b += n << 8 * (2-j)
        # Convert the 3 chars to four Base64 chars
        base64 += base64chars[ (b >> 18) & 63 ]
        base64 += base64chars[ (b >> 12) & 63 ]
        base64 += base64chars[ (b >> 6) & 63 ]
        base64 += base64chars[ b & 63 ]
    # Add the actual padding to the end
    if pad != 3:
        base64 = base64[:-pad]
        base64 += ending
    # Print the Base64 encoded result
    return base64


def base64decode(s):
  i = 0
  base64 = decoded = ''
  base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  # Replace padding with "A" characters so the decoder can process the string, and save the padding length for later
  if s[-2:] == '==':
    s = s[0:-2] + "AA"
    padd = 2
  elif s[-1:] == '=':
    s = s[0:-1] + "A"
    padd = 1
  else:
    padd = 0
  # Take 4 characters at a time
  while i < len(s):
    d = 0
    for j in range(0,4,1):

      d += base64chars.index( s[i] ) << (18 - j * 6)
      i += 1
    # Convert the 4 chars back to ASCII
    decoded += chr( (d >> 16 ) & 255 )
    decoded += chr( (d >> 8 ) & 255 )
    decoded += chr( d & 255 )
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