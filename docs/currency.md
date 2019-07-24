Billing documentation
=====================

Currency
--------

### Coins

**All currency units contain 100 coins.**
Regarding to the task we operate with USD, EUR, CAD, CNY.
All that currency have 100 coins in one banknote unit.
There are also some coins that have 1000 coins in one banknote unit like Rupees, etc.
But we have to not complicate the task.

**We store all amounts in coins as int values.**
So let's store all amounts in cents as
integer value, and we can always be sure that real amount in currency unit value
is stored amount (in coins) / 100.
