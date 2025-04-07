# John the Ripper: Password Cracker

John the Ripper is an Open Source password security auditing and password recovery tool 
available for many operating systems. 

## Setup
```
$ sudo apt install john
```

We can also use [Kali Linux](https://drive.google.com/drive/folders/1AzsF4Mvh1HJ8k6OW5W5hQ5CF0HdqA51l) in a virtual machine. 


## Cracking Linux Passwords

```bash
$ cat passwords-shadow.txt
student:$6$wRUypFSMS1P/TZ37$SmzPx5guncYyVOd368wi/YvTvWDPlzWtG1kEuVIrImp6tw502oPyOYNivBR/6QBeK18P9t.FG6QlEC2M9N.m01::0:99999:7:::

$ john passwords-shadow.txt    
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
student          (student)     
root66           (root)     
```

These cracked passwords will be stored in a file.

```bash
$ cat ~/.john/john.pot
$6$VGuJlIgFxyzSHUEE$x46AVxEIGKIPbesIPnJnJExKS9WTp2UeJo3ypjV2e7L/YBi6CsiF58FvN9xRtYwudPFhKPZRaAiv1XmY1YGpJ.:student
$6$/ggjIDVijkPEJ8MG$AQ1vRTVj20a2Sz3AXGiHWH821mC4IRbc3zp9I0W9p40xmjknfyicLPcSP9/ii8he8op1K.dz.4oQmzV8kiD7Y/:root66
```


## References
* [Youtube: Password Cracking With John The Ripper](https://youtu.be/XjVYl1Ts6XI)

* [John the Ripper Password Cracker](https://www.openwall.com/john/) 
	
* [10k Most Common Passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt)	

* [crunch - Wordlist Generator](https://sourceforge.net/p/crunch-wordlist/code/ci/master/tree/)

  
*Egon Teiniker, 2020-2025, GPL v3.0*	