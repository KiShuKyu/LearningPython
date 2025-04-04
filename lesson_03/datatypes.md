# Object types or Data types 

- Number : 1234, 3.14, 3+4j, 0b111, Decimal(),
Fraction()
# % remaninder hota h 
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))   
# always use []
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'burger', 'taste': 'yum'}, dict(hours=10) # key food : value spam

- Set : set('abc'), { 'a', 'b', 'c'}

- File : open('eggs.txt')

- Boolean : true and flase
- None : None
- Functions, modules, classes

- Advance : Decorators(existing fucntionality ko aaur powerful banne k kaam aate h), Generator, Iterators, Metaprogramming

# Numbers
# if a = 3 
a is variable 3 is memory and Memory ke andar data type hota h.
then 3 is the data type

# Floor and trunc 
(Floor hamesha neeche lekr jaega )
if math.floor(3.6)
    3
if math.floor(-3.6)
    -4

But, (trunc hamesha 0 ke pass lekr jaega)
if math.trunc(3.6)
    3
math.trunc(-3.6)
    -3


# Octal and hexal and binnary 
- to find octal value use (int('64', 8))
oct(64)
    0o100
- to find hexal value we use (int('64', 16))
hex(64)
    0x40
- to find binnary value we use (int('64', 2))
bin(64)
     0b1000000

random.randint(1, 100)
from decimal import Decimal
decimal('0.1')

# Lists [] (mutable)
tea_varities
["Black", "green", "Masala", "White"]
tea_varities_copy = tea_varities.copy()
- when we use .copy method we make a copy in memory
aagar hum tea_varitie me dete toh 1 ka mem 2 me bat jata x = 10 and y = 10 vrna x and y = 10 hota.

# Dictionaries {}

# Tuples (immutable) ()

