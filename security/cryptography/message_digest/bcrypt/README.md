# BCrypt

BCrypt is a password hashing algorithm designed by Niels Provos and David
Mazieres, based on the Blowfish cipher. It is specifically built for
storing passwords securely and has three properties that make it suitable
for this purpose:

* **Salted**: BCrypt automatically generates and embeds a random salt into
  every hash, so two identical passwords produce different hash values.
  This prevents precomputed rainbow table attacks.

* **Adaptive cost factor**: The algorithm accepts a `rounds` parameter
  (work factor) that controls how computationally expensive the hashing
  is. As hardware gets faster, the work factor can be increased to keep
  brute-force attacks impractical.

* **One-way**: Like all cryptographic hash functions, BCrypt cannot be
  reversed. Verification always re-hashes the candidate password and
  compares the result to the stored hash.

A BCrypt hash string looks like:

```
$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36zLtZ/G8k2NaF.iJO6FJLC
 |  |  |                     |
 |  |  salt (22 chars)       hash (31 chars)
 |  cost factor (rounds)
 version
```

## Setup

Install the `bcrypt` library with pip:

```bash
$ pip install bcrypt
```

## Using BCrypt

### `bcrypt.gensalt(rounds=12)`

Generates a random salt. The optional `rounds` parameter sets the cost
factor (default: 12). Higher values make hashing slower and more resistant
to brute-force attacks.

```python
salt = bcrypt.gensalt()
```

### `bcrypt.hashpw(password, salt)`

Hashes `password` (must be `bytes`) using the given `salt`. The salt is
embedded in the returned hash, so it does not need to be stored separately.

```python
hashed = bcrypt.hashpw(b's$cret12', salt)
```

### `bcrypt.checkpw(password, hashed)`

Verifies a plaintext `password` against a stored `hashed` value. It
extracts the salt from `hashed`, re-hashes the candidate password, and
returns `True` if the hashes match.

```python
bcrypt.checkpw(b's$cret12', hashed)  # True
bcrypt.checkpw(b'wrongpassword', hashed)  # False
```

### Example

```python
import bcrypt

password = b's$cret12'
salt   = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

assert bcrypt.checkpw(password, hashed)           # valid password
assert not bcrypt.checkpw(b'wrongpassword', hashed)  # invalid password
```

## References

* [GitHub: bcrypt](https://github.com/pyca/bcrypt/)


*Egon Teiniker, 2016-2026, GPL v3.0*

