"""
alphabet, lexis, Syntax, Semantics
an alphabet: a set of symbols used to build words of a certain language
(e.g., the Latin alphabet for English, the Cyrillic alphabet for Russian,
Kanji for Japanese, and so on)

a lexis: (aka a dictionary) a set of words the language offers its users
(e.g., the word "computer" comes from the English language dictionary,
while "cmoptrue" doesn't; the word "chat" is present both in English and
French dictionaries, but their meanings are different)

a syntax: a set of rules (formal or informal, written or felt intuitively)
used to determine if a certain string of words forms a valid sentence
(e.g., "I am a python" is a syntactically correct phrase,
while "I a python am" isn't)

semantics: a set of rules determining if a certain phrase makes sense
(e.g., "I ate a doughnut" makes sense, but "A doughnut ate me" doesn't)

# Python program to demonstrate semantic error
import sys
# Driver Code
if __name__ == '__main__':
    # exit() statement before cout
    sys.exit(0);
    # Print the value
    print("GFG!");

This program has no syntax error as it is following every programming rule
but still, it will not print anything on the screen because the return
statement is written before the print statement which causes the program
to terminate before printing anything on the screen.
This type of situation is considered a semantic error.
"""

"""
Some framework in python eco system
Software Development (build control, management, and testing - Scons, Buildbot, Apache Gump, Roundup, Trac)
Web and Internet development (e.g., Django and Pyramid frameworks, Flask and Bottle micro-frameworks)
"""

"""
compilation and interpretation
A compiled language is a programming language that is generally compiled and not interpreted. 
It is one where the program, once compiled, is expressed in the instructions of the target machine; 
this machine code is undecipherable by humans. Types of compiled language – C, C++, C#, CLEO, COBOL, etc.

An interpreted language is a programming language that is generally interpreted, 
without compiling a program into machine instructions. 
It is one where the instructions are not directly executed by the target machine, but instead, 
read and executed by some other program. Interpreted language ranges – JavaScript, Perl, Python, BASIC, etc.

Java is kind of both. Firstly java compiled(some would prefer to say "translated") to bytecode, 
which then either compiled, or interpreted by JIT.
"""


"""
Computers have their own language, too, called machine language, which is very rudimentary.
Python is an interpreted language. If you want to program in Python, you'll need the Python interpreter.

Due to historical reasons, languages designed to be utilized in the interpretation manner are often called
scripting languages, while the source programs encoded using them are called scripts. 
E.g. Javascript, PHP, Python, Perl, Ruby, Groovy
"""

"""
ARM64 vs X64

X64 CPUs are fast and powerful, but they require a lot of electricity. So, they are usually used in laptops. 
ARM CPUs are weak but low-power processors for smartphones and other mobile devices. 
Apple has released M1/2 laptops based on ARM CPUs and they have strong performance. 
Many poeple think the future is moving to ARM CPUs.
"""

"""
There are the Pythons which are maintained by the people gathered 
around the PSF (Python Software Foundation), a community that aims to develop, improve, expand, 
and popularize Python and its environment. 
The PSF's president is Guido von Rossum himself, and for this reason, these Pythons are called canonical. 
They are also considered to be reference Pythons, 
as any other implementation of the language should follow all standards established by the PSF.

Guido van Rossum used the "C" programming language to implement the very first version of his language and this decision 
is still in force. All Pythons coming from the PSF are written in the "C" language.

It is important to remember that there may be smaller or bigger differences between subsequent Python 3 releases 
(e.g., Python 3.6 introduced ordered dictionary keys by default under the CPython implementation) – 
the good news, though, 
is that all the newer versions of Python 3 are backward compatible with the previous versions of Python 3.

Backward compatible means that code written for one version of Python 3 should generally
 work correctly when run on a later version of Python 3.

Cython: Cython is intended to do – to automatically translate the Python code (clean and clear, but not too swift) 
into "C" code (complicated and talkative, but agile).

Jython: "J" is for "Java". Imagine a Python written in Java instead of C. 
This is useful, for example, if you develop large and complex systems written entirely in Java 
and want to add some Python flexibility to them. 
The traditional CPython may be difficult to integrate into such an environment, 
as C and Java live in completely different worlds and don't share many common ideas.
Jython can communicate with existing Java infrastructure more effectively. 
This is why some projects find it useful and necessary.
"""
