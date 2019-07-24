Billing documentation
=====================

Currency
--------

### Coins

**All currency units contain 100 coins.**
Regarding to the task we operate with
[**USD**](https://en.wikipedia.org/wiki/United_States_dollar),
[**EUR**](https://es.wikipedia.org/wiki/Euro),
[**CAD**](https://en.wikipedia.org/wiki/Canadian_dollar),
[**CNY**](https://en.wikipedia.org/wiki/Renminbi).
All that currency have 100 coins in one banknote unit.
There are also some coins that have 1000 coins in one banknote unit like Rupees, etc.
But we have to not complicate the task.

If you wanna work with other currencies which units contains another count of sub units, this schema should be change.
Probably you would like to store currency exponent value like 2 (100 cents in 1 dollar), 3 (1000 cents in 1 dollar), etc.

**We store all amounts in coins as int values.**
So let's store all amounts in cents as
integer value, and we can always be sure that real amount in currency unit value
is stored amount (in coins) / 100.
