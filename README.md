# CS4400 / CS7NS1: Infernoballs

Group Members:
1. [Ciarán Ingle](https://github.com/inglec)
2. [Deprub Chakraborty](https://github.com/rupdeb)
3. [Sridhar Amirneni](https://github.com/sridharamirneni)
4. [Suprith Ramesh](https://github.com/suprithramesh)

[Link](https://github.com/sftcd/cs7ns1/tree/master/assignments/practical5) to the assignment's GitHub repo.

## Hashes

### Methods

Wordlists & masks:
1. Five lowercase letters (Generated using `pwgen -0 -A 5`)
2. Two four-letter words concatenated (Generated from English dictionaries in Ubuntu's `/usr/share/dicts/words/`)
3. [rockyou.txt](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2)

### Formats

I've formatted the hashes as follows: `share:hash`.

Type | Command
---- | -------
PBKDF2-HMAC-SHA256 | `john --format=PBKDF2-HMAC-SHA256-opencl --wordlist=<wordlist> <filename>`
sha1crypt | `john --format=sha1crypt-opencl --wordlist=<wordlist> <filename>`
sha512crypt | `john --format=sha512crypt-opencl --wordlist=<wordlist> <filename>`<br/>`hashcat -a 0 -w 4 -O -m 1800 --username <wordlist> <filename>`
argon2i | `john --format=argon2 --wordlist=<wordlist> <filename>`

### Hashrates

#### John The Ripper

Type | Device | Hashrate
---- | ------ | --------
PBKDF2-HMAC-SHA256 | P100 <br/> 1080Ti <br/> c5.9x | `40,000c/S` <br/> TODO <br/> `17,700c/S`
sha1crypt | P100 <br/> 1080Ti <br/> c5.9x | `7,060c/S` <br/> TODO <br/> `2,500c/S`
sha512crypt | P100 <br/> 1080Ti <br/> c5.9x | TODO <br/> TODO <br/> `600c/S`
argon2i | c5.9x | `100c/S`

#### Hashcat

Type | Device | Hashrate
---- | ------ | --------
sha512crypt | P100 <br/> 1080Ti <br/> c5.9x | TODO <br/> TODO <br/> `600c/S`

### Software

JohnTheRipper seems to work better than Hashcat for PBKDF2 hashes.

Otherwise, Hashcat appears to be better.

### Progress

#### Level 1

Level 1 seems to only require `rockyou.txt`.

Type | Amount
---- | -------
PBKDF2-HMAC-SHA256 | 65/65
sha1crypt | 0/50
sha512crypt | 0/58
argon2i | 0/56

## Instances

### AWS / RosettaHub

The `c5.9xlarge` instance seems to be the best CPU instance you can rent. It is a 32-thread CPU with AVX-512.

This is the best instance for cracking Argon2.

### Google Cloud Platform

Google Cloud Platform's [Compute Engine](https://console.cloud.google.com/compute/) offers $300 free credit.

A custom instance with two threads and a single P100 GPU seems to be the best overall instance for cracking everything apart from Argon2. Certain regions such as `europe-west2` will **not** allow you to access a GPU instance.

I would recommend `europe-west1`.

You are limited to a single GPU across all instances unless you request a limit increase.

## Meetings

Date | Time | Location | Description
---- | ---- | -------- | -----------
23/10 | 12:00 | South Leinster St. | Initial meeting
30/10 | 18:00 | South Leinster St. | Infernoballs released
