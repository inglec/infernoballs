# CS4400 / CS7NS1: Infernoballs

Group Members:
1. [Ciarán Ingle](https://github.com/inglec)
2. [Deprub Chakraborty](https://github.com/rupdeb)
3. [Sridhar Amirneni](https://github.com/sridharamirneni)
4. [Suprith Ramesh](https://github.com/suprithramesh)

[Link](https://github.com/sftcd/cs7ns1/tree/master/assignments/practical5) to the assignment's GitHub repo.

## Scripts

Python dependencies for `as5-makeinferno.py`:

```
sudo apt install python-pip

sudo -H pip install secretsharing jsonpickle passlib argon2_cffi pycrypto

```

Potfile to broken format (Only required for Hashcat):
```
python brokenToPotfile.py <potfile> > output.broken
```

Combine all hash files:

```
cat *.broken | sort | uniq > all.broken
```

Decrypting the ciphertext for a given level:

```
./as5-makeinferno.py -t decrypt -c <path_to_ciphertext> -b <path_to_broken> -H <path_to_hashes> [-o <path_to_output>]

# Sample usage
./as5-makeinferno.py -t decrypt -c ciphertexts/ciphertext1.txt -b broken/all.broken -H hashes/infernoball1.hashes -o infernoballs/infernoball2.as5
```

Get hashes from infernoball:

```
python getHashesFromJSON <infernoball> > infernoballN.broken
```

Get ciphertext from infernoball:

```
python getCiphertextFromJSON <infernoball> > ciphertextN.txt
```


## Hashes

### Methods

Wordlists & masks:
1. Five lowercase letters (Generated using `pwgen -0 -A 5`)
2. Two four-letter words concatenated (Generated from English dictionaries in Ubuntu's `/usr/share/dicts/words/`)
3. [rockyou.txt](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2)

### Formats

I've formatted the hashes as follows: `share:hash`.

| Type               | Command                                                                            |
|:------------------ |:---------------------------------------------------------------------------------- |
| PBKDF2-HMAC-SHA256 | `jtr/run/john --format=PBKDF2-HMAC-SHA256-opencl --wordlist=<wordlist> <filename>` |
| sha1crypt          | `jtr/run/john --format=sha1crypt-opencl --wordlist=<wordlist> <filename>`          |
| sha512crypt        | `jtr/run/john --format=sha512crypt-opencl --wordlist=<wordlist> <filename>`        |
|                    | `hashcat -a 0 -w 4 -O -m 1800 --username <wordlist> <filename>`                    |
| argon2i            | `jtr/run/john --format=argon2 --wordlist=<wordlist> <filename>`                    |

### Hashrates

#### John The Ripper

| Type               | Device | Hashrate  |
|:------------------ |:------:| ---------:|
| PBKDF2-HMAC-SHA256 | P100   | 40,000c/S |
|                    | 1080Ti | TODO      |
|                    | c5.9x  | 17,700c/S |
| sha1crypt          | P100   | 7,060c/S  |
|                    | 1080Ti | TODO      |
|                    | c5.9x  | 2,500c/S  |
| sha512crypt        | P100   | 700c/S    |
|                    | 1080Ti | TODO      |
|                    | c5.9x  | 600c/S    |
| argon2i            | c5.9x  | 100c/S    |

#### Hashcat

| Type        | Device | Hashrate |
|:----------- |:------:| --------:|
| sha512crypt | P100   | 1170H/s  |
|             | 1080Ti | 150H/s   |

### Software

JohnTheRipper seems to work better than Hashcat for PBKDF2 hashes.

Otherwise, Hashcat appears to be better.

### Progress

#### Level 1

Level 1 seems to only require `rockyou.txt`.

| Type               | Amount  |
|:------------------ |:-------:|
| PBKDF2-HMAC-SHA256 | 65/65   |
| sha1crypt          | 50/50   |
| sha512crypt        | 44/58   |
| argon2i            | 0/56    |

PBKDF2-HMAC-SHA256:

1. `rockyou.txt`: 65 cracked. (Ciarán)

sha1crypt:

1. `five.txt`: 0 cracked. (Ciarán)
2. `fourfour.txt`: 0 cracked. (Ciarán)
3. `rockyou_9char.txt`: 0 cracked. (Ciarán)
4. `rockyou_7char.txt`: 10 cracked. (Ciarán)
5. `rockyou_6char.txt`: 17 cracked. (Ciarán)
6. `rockyou_5char.txt`: 1 cracked. (Ciarán)
7. `rockyou_8char.txt`: 22 cracked. (Ciarán)

sha512crypt:

1. `rockyou_2char.txt`: 0 cracked. (Sridhar)
2. `rockyou_3char.txt`: 0 cracked. (Sridhar)
3. `rockyou_4char.txt`: 0 cracked. (Sridhar)
4. `rockyou_5char.txt`: 2 cracked. (Sridhar)
5. `rockyou_6char.txt`: 12 cracked (Debrup)
6. `rockyou_7char.txt`: 17 cracked (Sridhar)
7. `rockyou_8char.txt`: 13 cracked (Debrup)

argon2i:
1. `rockyou_5char.txt`: In progress... (Ciarán)

## Instances

Clone the Git repo:

```
git clone https://github.com/inglec/infernoballs
```

### AWS / RosettaHub

The `c5.9xlarge` instance seems to be the best CPU instance you can rent. It is a 32-thread CPU with AVX-512.

This is the best instance for cracking Argon2.

### Google Cloud Platform

I moved the setup guide to [here](https://github.com/inglec/Google-Cloud-Cracking-Setup).

## Meetings

| Date  | Time  | Location           | Description           |
|:-----:|:-----:|:------------------ |:--------------------- |
| 23/10 | 12:00 | South Leinster St. | Initial meeting       |
| 30/10 | 18:00 | South Leinster St. | Infernoballs released |
