# Setup Cryptographic Libraries in Python

The following libraries and tools are used in the Virtual Lab to run the cryptography examples.

## pyca/cryptography
Cryptography  includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions.
```
$ pip3 install cryptography
```

Note that on Kali Linux an **old version** is already installed.
In that case, we have to update the library:
```
$ pip3 install cryptography --upgrade
Successfully installed cffi-1.14.3 cryptography-3.1.1 pycparser-2.20
```

## BCrypt Library

Good password hashing for your software and your servers

```
$ pip3 install bcrypt
```

## PyJWT Library

PyJWT is a Python library which allows you to encode and decode JSON Web Tokens (JWT). JWT is an open, industry-standard (RFC 7519) for representing claims securely between two parties.

```
$ pip3 install pyjwt
```



## References
* [cryptography](https://cryptography.io/en/latest/)

* [bcrypt](https://github.com/pyca/bcrypt/)

* [PyJWT](https://github.com/jpadilla/pyjwt)
* [PyJWT Documentation](https://pyjwt.readthedocs.io/en/stable/)

*Egon Teiniker, 2020-2023, GPL v3.0*
