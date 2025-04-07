# Random Numbers

**Randomness is found everywhere in cryptography**: in the generation of secret keys, in encryption schemes, and even in the attacks on cryptosystems. 
Without randomness, cryptography would be impossible because all operations would become predictable, 
and therefore insecure.

To generate randomness, we need two things:
* A source of uncertainty, or source of entropy, provided by **random number generators (RNGs)**. 
* A cryptographic algorithm to produce high-quality random bits from the source of entropy. 
   This is found in **pseudorandom number generators (PRNGs)**.

In cryptography, randomness usually comes from RNGs, which are software or hardware components 
that leverage entropy in the analog world to produce unpredictable bits in a digital system.


Note that PRNGs rely on RNGs but behave differently: RNGs produce true random bits relatively slowly 
from analog sources, in a nondeterministic way, and with no guarantee of high entropy. 
In contrast, PRNGs produce random-looking bits quickly from digital sources, in a deterministic way, 
and with maximum entropy. 

**PRNGs transform a few unreliable random bits into a long stream of reliable pseudorandom 
bits suitable for crypto applications**.


## Cryptographic vs. Non-Cryptographic PRNGs

Non-crypto PRNGs are designed to produce uniform distributions for applications such as scientific 
simulations or video games. However, we should **never use non-crypto PRNGs in crypto applications**, 
because they’re insecure—they’re only concerned with the quality of the bits’ probability distribution 
and not with their predictability. 

Crypto PRNGs, on the other hand, are unpredictable, because they’re also concerned with the strength of the 
underlying operations used to deliver well-distributed bits. 
Unfortunately, most PRNGs exposed by programming languages, such as libc’s `rand()` and Python’s `random` module 
are non-cryptographic.

_Example_: Non-cryptographic PRNG from the `random` module  
```Python
def test_randint(self):
    random.seed(1)  # if no value is given, the current system time is used
    b = random.randint(0, 1000)
    print(b)
```

Note that the **same seed results in the same random number**!!
The pseudo-random generators of the `random` module should not be used for security purposes.


## Generate Secure Random Numbers

Python's `secrets` module is used for generating cryptographically strong random numbers suitable 
for managing data such as passwords, account authentication, security tokens, and related secrets.

_Example_: Cryptographically secure PRNG in Python 
```Python
def test_random_token_hex(self):
        token = secrets.token_hex(32)
        print(token)
```
To retrieve random data from `secrets`, we can use the following methods:

* `token_bytes([nbytes=None])`: Return a random byte string containing `nbytes` number of bytes. 

* `token_hex([nbytes=None])`: Return a random text string, in hexadecimal. 
    The string has `nbytes` random bytes, each byte converted to two hex digits. 

* `token_urlsafe([nbytes=None])`: Return a random URL-safe text string, containing `nbytes` random bytes. 
    The text is **Base64 encoded**. 

If `nbytes` is `None` or not supplied, a reasonable default is used.


## OpenSSL: Generating Psuedo Random Numbers 
The following command line generates a number of random bytes, which can either be output raw, as `Base64` or as `HEX`:
```
$ openssl rand -hex 16
f05a4f9bef09d057c355c6e28fec5543

$ openssl rand -base64 16
gokRIzPgvBsnQd5fshD9fg==
```
Parameters:
* **rand**: Generate pseudo-random bytes.
* **-hex**: Show the output as a hex string.
* **-base64**: Perform base64 encoding on the output.
* **-out file**: Write to file instead of standard output.

This command generates random bytes using a **cryptographically secure pseudo random number generator (CSPRNG)**.


## References

* [secrets — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)

* Jean-Philippe Aumasson. Serious Cryptography. No Starch Press, 2018
    * Chapter 2: Randomness

*Egon Teiniker, 2020-2024, GPL v3.0*    