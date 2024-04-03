# Challenge
>Just like with ASCII, there's an almost endless amount of ways to interpret data.
>
>When a lot of people agree on an interpretation, it's called a standard.
>
>They're often established and documented in Requests for Comments (RFCs).
>
>A widely used standard is Base64 (https://www.rfc-editor.org/rfc/rfc4648).
>
>Since RFCs and Base64 weren't magical enough, we made our own suggestion through Request for Magic (RFM) number #15928 for MAGI64.
>
>Submit the solution as flag{some-text-here}.
>
>Author: KatSilverberg
# Solution
This challenge is to decode a flag encoded with base64. However, it is encoded with a custom character set, and we are given a [list] with the new character set. 
The encoding process is the same as regular base64 despite the different character set, so we can simply subsitute the characters of the encoded flag with those of the standard base64 character set.

![Python example solution](Files/encoding_løsning.py)

This script returns the flag:
>flag{ikke-så-ulikt-base64-egentlig}
