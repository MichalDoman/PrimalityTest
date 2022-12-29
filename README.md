# PrimalityTest (own project)

___

### How to use it:

This app examines whether a given number is prime or composite. When the program is launched, in the terminal there will
appear a starting screen. To use the app, type in a number and click enter.

```
-----------------------------------------------------------
             Welcome to Primality Test App!
Type in a number that you want to examine, and press ENTER:
-----------------------------------------------------------

Your number:
```

### Outcome:

Depending on the input, outcome may differ. If input is correct, the program will calculate all of the factors that the
given number has. In case of the number not being prime, the app finds two additional primes: one that is the closest to
the given number and is smaller, and one that is the closest but bigger. Here is an example:

```
Your number: 987
987 IS NOT a prime number, it is composite.
It can be divided by [1, 3, 7, 21, 47, 141, 329, 987].
So, there are 8 factors.
The closest prime number smaller than 987, is 985.
And the closest bigger, is 989.
```
