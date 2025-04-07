How to create private and public key using OpenSSL?
---------------------------------------------------

$ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out openssl-private-key.pem

$ openssl pkey -in openssl-private-key.pem -out openssl-public-key.pem -pubout

