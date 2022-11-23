# Project Euler example solutions

This repo contains example solutions to Project Euler problems 5, 35 and 81. Problem 5 is done with Java and problems 35 & 81 with Python

# Tools
As code editor I have used VS Code myself, you can install it for free from https://code.visualstudio.com/download.

To run your code you can install following command line tools:
- Python: https://www.python.org/downloads/
    - note that most Linux distros include Python pre-built
    - online: http://pythonfiddle.com/
- Java: https://www.java.com/en/download/help/download_options.html
    - online: https://www.mycompiler.io/online-java-compiler

## JAVA solution

Single source file java code can also be very easy to work with. Just install java environment and:

```
java .\p5_euler.java
```

### Problem #005
https://projecteuler.net/problem=5

Source: https://github.com/vilikilpe/euler/blob/main/p5_euler.java

```
Solution to Euler problem #005 is 232792560
```

First time coding with Java. Just looping as long as the result is found. Execution time increases rapidly when n is increaced. There are many options to reduce execution time, for example reducing the needed checks.

## Python solutions
Python is a very easy language to work with. If you have installed Python (3.8 or newer), then execute the code simply by:

```
python .\p35_euler.py
```

There are also tests for both Python solution files. Tests are implemented with pytest, so it's need to be installed. There is a Pipfile which handles installation. 

1. Install
```
pipenv install
```
2. Start virtual env
```
pipenv shell
```
3. Tests can be run easily by a single command
```
pytest
```
### Problem #035
https://projecteuler.net/problem=35

Source: https://github.com/vilikilpe/euler/blob/main/p35_euler.py

```
Solution to Euler problem #035 is 55
```

Problem 35 is solved with two different ways. There are basically two versions of the primes-function which finds all prime number below the given number. The better version (v2) in left as a default. Primes-function took majority of the run time (analyzed with https://pypi.org/project/snakeviz/) so it was focused to optimize that one. prime_v2 exucution time is more or less linear when n is increacred. 

Comparison between two algorithms:
| algorithm | s |
| --- | --- |
| 1 | 3.06 |
| 2 | 0.65 |

### Problem #081
https://projecteuler.net/problem=81

Source: https://github.com/vilikilpe/euler/blob/main/p81_euler.py

```
Solution to Euler problem #081 is 427337
```

There is a matrix.txt file for this problem. It is a 80x80 matrix where every single matrix value is an integer (converted in the soution). Tests are run with smaller matrices. Execution time on the solution was 83 ms.
