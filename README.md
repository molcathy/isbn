# isbn

Write a program that finds the check number for a given ISBNs

* takes 12 digits numbers
* multiplies each
    - odd  digit with 1
    - even digit with 3
* adds the results of the 2 multiplications
* find the remainder of the addition divided by ten
* if the remainder:
    - is equal to 0 then 0 is the check number (see https://en.wikipedia.org/wiki/Check_digit#UPC)
    - else subtracts the remainder from 10 which to finds the check number

Test your program with the following ISBNs:
* 978110754673 --check-number--> 8
* 978191052307 --check-number--> 0

Screenshot your program code and the output for both the ISBNs.


Please check
* note that "ISBN 13" uses same method as [UPC](https://en.wikipedia.org/wiki/Check_digit#UPC)
* [online ISBN 13 calculator](http://www.hahnlibrary.net/libraries/isbncalc.html)

```
## RULES TO VALIDATE ISBN 13
1. Add the digits in the odd-numbered positions from the right (first, third, fifth, etc. - not including the check digit) together and multiply by three.
2. Add the digits (up to but not including the check digit) in the even-numbered positions (second, fourth, sixth, etc.) to the result.
3. Take the remainder of the result divided by 10 (modulo operation). If the remainder is equal to 0 then use 0 as the check digit, and if not 0 subtract the remainder from 10 to derive the check digit.
```