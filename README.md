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
python formatter.py [HASHES] [POTFILE] > output.broken
```

Combine all hash files:
```
cat *.broken | sort | uniq > all.broken
```

Decrypting the ciphertext for a given level:
```
./as5-makeinferno.py -t decrypt -i [INFERNOBALL] -b [BROKEN]
```

This will write three files:
1. `infernoballN.as5`
2. `infernoballN.secrets`
3. `infernoballN.hashes`

#### Regex

[This](https://regexr.com/) website is really useful for learning and testing Regex.

Get all words of length 5-8:
```
cat [FILE] | egrep "^.{5,8}$"
```

Get words of length 5-8 with just lowercase:
```
cat [FILE] | egrep "^[a-z]{5,8}$"
```

Get words of length 5-8 with just uppercase and digits:
```
cat [FILE] | egrep "^([0-9]|[A-Z]){5,8}$"
```

#### Crackstation

Download and extract [Crackstation](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) wordlist:
```
wget https://crackstation.net/files/crackstation.txt.gz
gunzip crackstation.txt.gz
```

## Hashes

### Methods

#### Level 1

Uses the [rockyou.txt](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2) wordlist.

Hints:
* All words are between **5-8 characters** in length.

#### Level 2

Uses wordlist of two four-letter words concatenated, referencing [this](https://xkcd.com/936/) XKCD comic.

These words originate from Unix's `/usr/share/dicts/words/`.

Hints:
* In all words, the second four-letter word begins with an **uppercase** letter.

#### Level 3

Uses wordlist generated from `pwgen -A 5`.

Hints:
* All words are exactly **5 characters** in length.
* All words contains **at least** one vowel.
* All words contains **exactly** one digit.
* In each word, the digit is positioned at one of the **last three** indices.

#### Level 4

Uses wordlist scraped from the [SCSS](https://www.scss.tcd.ie//) and [Trinity](https://www.tcd.ie/) websites.

Hints:
* Can use [CeWL](https://github.com/digininja/CeWL/) to crawl websites for words.

#### Level 5

Uses wordlist of Submitty usernames.

Hints:
* Submitty usernames can be cracked from the [SHA256 list](https://github.com/sftcd/cs7ns1/blob/master/assignments/practical5/TeamSelection.md#pool-of-students) of students.
* Alternatively, all student names can be [found](https://tcd.blackboard.com/webapps/blackboard/execute/displayEmail?navItem=email_select_students&course_id=_52594_1) on BlackBoard.

#### Level 6

Same as Level 1.

#### Level 7

Uses wordlist of [keyboard walks](https://cyberarms.wordpress.com/2018/02/13/creating-hashcat-keymap-walking-password-wordlists/).

Hints:
* Use [KwProcessor](https://github.com/hashcat/kwprocessor.git) to generate wordlist.

#### Level 8

Same as Level 1.

#### Level 9

Uses [Crackstation](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) wordlist.

Get alphanumeric 5-8 character list:
```
egrep -a "^[a-zA-Z0-9]{5,8}$" crackstation.txt > alphanumeric.txt
```

Possible regexes:
1. All numbers (111M entries):
```
egrep "^[0-9]+$" alphanumeric.txt > output.txt
```
2. 1 number + lowercase (13M entries):
```
egrep "^[0-9][a-z]+$" alphanumeric.txt > output.txt
```
3. 3 numbers + 5 letters (1M entries):
```
egrep "^[0-9]{3}[a-zA-Z]{5}$" alphanumeric.txt > output.txt
```

### Formats

I've formatted the hashes as follows: `share:hash`.

| Type               | Command                                                                          |
|:------------------ |:-------------------------------------------------------------------------------- |
| PBKDF2-HMAC-SHA256 | `jtr/run/john --format=PBKDF2-HMAC-SHA256-opencl --wordlist=[WORDLIST] [HASHES]` |
| sha1crypt          | `jtr/run/john --format=sha1crypt-opencl --wordlist=[WORDLIST] [HASHES]`          |
| sha512crypt        | `jtr/run/john --format=sha512crypt-opencl --wordlist=[WORDLIST] [HASHES]`        |
|                    | `hashcat -a 0 -w 4 -O -m 1800 --username [WORDLIST] [HASHES]`                    |
| argon2i            | `jtr/run/john --format=argon2 --wordlist=[WORDLIST] [HASHES]`                    |

### Hashrates

#### John The Ripper

| Type               | Device | Hashrate  |
|:------------------ |:------:| ---------:|
| PBKDF2-HMAC-SHA256 | P100   | 45,000c/S |
|                    | c5.9x  | 17,700c/S |
| sha1crypt          | P100   | 7,060c/S  |
|                    | c5.9x  | 2,500c/S  |
| sha512crypt        | P100   | 700c/S    |
|                    | c5.9x  | 600c/S    |
| argon2i            | c5.9x  | 100c/S    |

#### Hashcat

| Type        | Device | Hashrate |
|:----------- |:------:| --------:|
| sha512crypt | P100   | 1170H/s  |

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
