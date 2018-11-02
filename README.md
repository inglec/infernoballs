# CS4400 / CS7NS1: Infernoballs

Team 3 Members:
1. [Ciarán Ingle](https://github.com/inglec)
2. [Debrup Chakraborty](https://github.com/rupdeb)
3. [Sridhar Amirneni](https://github.com/sridharamirneni)
4. [Suprith Ramesh](https://github.com/suprithramesh)

[Link](https://github.com/sftcd/cs7ns1/tree/master/assignments/practical5) to the assignment's GitHub repo.

The leaderboard is [here](https://down.dsg.cs.tcd.ie/cs7ns1-leaderboard/).

## Scripts

Python dependencies for `as5-makeinferno.py`:
```
sudo apt install python-pip

sudo -H pip install secretsharing jsonpickle passlib argon2_cffi pycrypto
```

Potfile to broken format (Only required for Hashcat):
```
python formatter.py <hashes> <potfile> > output.broken
```

Combine all hash files:
```
cat *.broken | sort | uniq > all.broken
```

Decrypting the ciphertext for a given level:
```
./as5-makeinferno.py -t decrypt -i <infernoball> -b <broken>

# Sample usage
./as5-makeinferno.py -t decrypt -i infernoballs/infernoball1.as5 -b broken/level1/all.broken
```

This will write three files:
1. `infernoballN.as5`
2. `infernoballN.secrets`
3. `infernoballN.hashes`

## Hashes

### Methods

#### Level 1

Wordlist:
* [rockyou.txt](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2)

Constraints:
* 5-8 characters.

#### Level 2

Wordlist:
* Two four-letter words concatenated.
* Ubuntu's `/usr/share/dicts/words/`.

Constraints:
* Second word begins with an uppercase letter.

#### Level 3

`pwgen -A 5`

Constraints:
* **At least** one vowel.
* **Exactly** one digit.
* The digit at one of the last three indices.

#### Level 4

Words scraped from the [SCSS](https://www.scss.tcd.ie//) and [Trinity](https://www.tcd.ie/) websites.

#### Level 5

Submitty usernames.

Can be "found" on BlackBoard.

#### Level 6

Same as Level 1.

#### Level 7

Keyboard patterns (WIP).

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
