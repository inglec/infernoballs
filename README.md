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

### Software

JohnTheRipper seems to work better than Hashcat for PBKDF2 hashes.

Otherwise, Hashcat appears to be better.

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

Date | Time | Description
---- | ---- | -----------
23/10 | 12:00 | Initial meeting
30/10 | 13:00 | Infernoballs released

## Tasks

Todo:
1. Make a wordlist from Dante's Inferno.
