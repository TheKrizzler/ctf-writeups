# Data Representation
## Challenge
>In computers everything is bits, and a bit can be either 0 or 1.
>
>In order for computers to function, not to mention talk together, we need a common understanding of how to interpret an order of bits as text, images, video etc.
>
>When there are many bits in a row, like in 0010101010110101010100001010101, a rewrite to decimal or hexadecimal numbers makes it shorter and more readable.
>
>ASCII is a magic standard for converting bits to text. You'll find a table showing how to convert decimal, hexadecimal and octal numbers to text in the attached textbook. Your challenge is to convert the word "magi" to both bits, hexadecimal and decimal.
>
>Submit the solution as flag{bits,hexadecimal,decimal}.
>
>Example: flag{01101000011001010110100100100001,0x68656921,1751476513}
>
>Author: KatSilverberg

## Solution
This was a very simple challenge, but i was still stuck on it for a few days due to a small detail. To convert the word "magi" to binary, hex, and decimal we can use a service like [rapidtables](https://www.rapidtables.com/convert/number/ascii-to-binary.html).

Note that the decimal value in the example is **not** put together of the four separate decimal values that represent the string "magi", but rather the decimal representation of the value of the hex number next to it. For this reason we will do the same thing in the flag.

Binary: 01101101 01100001 01100111 01101001  
Hex: 0x6d616769  
Decimal: 1835100009 (Found by converting either the hex or binary value to decimal, **not** the string.  

>flag{01101101011000010110011101101001,0x6d616769,1835100009}

*IMPORTANT: The flag must be submitted with only lower-case letters. This is the detail that took me a while to figure out.*
