pymutate
========

A really simple string mutator that takes piped input and messes it up... for science!

*Story*:
I needed an easy way to do mutation fuzzing for work.  That is, rather than
generating purely random data for testing, I wanted to modify (mutate) an
existing string. Fuzz testing has been around for a long time, and I'm sure I
could have found code for this online, but after a couple of google searches
didn't turn it up, I realized it would probably take less time for me to just
write the darned code myself than find someone else's.

I'm sharing this in hopes that the next person who wants what I want will find
it and save themselves the time.

*License*:
Eventually I'll choose a proper open source license for this, but the short
version is that this code was meant to be used and shared freely and I'd like it
if you could attribute it to me and let me know if you use it.  You are
expressly forbidden to use it to cheat on class assignments that require you to
build a fuzz tester (feel free to learn from it, just don't claim it as your
own work!)

Usage:
-----
usage: pymutate.py [-h] [--insert] [--delete] [--mutate] [--crossover] [--all]

A string mutation device for piped data

optional arguments:
  -h, --help   show this help message and exit
  --insert     Insert a random character in a random location
  --delete     Delete character in a random location
  --mutate     Mutate a random character in a random location
  --crossover  Cross two random characters
  --all        Show all possible mutation types

If nothing is specified, pymutate chooses a mutation type randomly (equal chance
of insert, delete, mutate, crossover) and outputs the result.  Perhaps one day
there will be specifiable percentages for this.


 Terri Oda
 terri@zone12.com
