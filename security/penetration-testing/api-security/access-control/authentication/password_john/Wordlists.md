# Wordlists

Wordlists are used to **crack passwords**. But we can also check user passwords
against a list of common passwords to reject week choices.

## Most Common Passwords Lists

    https://github.com/DavidWittman/wpxmlrpcbrute/blob/master/wordlists/1000-most-common-passwords.txt
```   
    123456
    password
    12345678
    qwerty
    123456789
    12345
    1234
    111111
    1234567
    dragon
    123123
    baseball
    abc123
    football
    monkey
    letmein
    696969
    shadow
    master
    666666
    qwertyuiop
    123321
    mustang
    1234567890
    michael
    ...
```
   
    https://www.passwordrandom.com/most-popular-passwords


## Generate Wordlists

To calculate a table of hash values, we can generate a permutation of strings
using crunch:
```
    crunch <min-len> <max-len> [<charset string>] [options]
```
* min-len: The minimum length string you want crunch to start at.
             This option is required even for parameters that won't use the value.

* max-len: The maximum length string you want crunch to end at.
             This option is required even for parameters that won't use the value.

* charset string: You may specify character sets for crunch to use on the command
              line or if you leave it blank crunch will use the default character sets.
              The order MUST BE lower case characters, upper case characters, numbers, and
              then symbols.
              If you don't follow this order you will not get the results you want.
              You MUST specify either values for the character type or a plus sign.

Example: All strings of length 4
```
    $ crunch 4 4 -o wordlist.txt
    aaaa
    aaab
    aaac
    aaad
    aaae
    aaaf
    aaag
    aaah
    aaai
    aaaj
    aaak
    aaal
    aaam
    aaan
    aaao
    aaap
    aaaq
    aaar
    aaas
    aaat
    aaau
    aaav
    aaaw
    aaax
    aaay
    aaaz
    aaba
    ...    
```
