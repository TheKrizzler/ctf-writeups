# Challenge
>In this challenge I have implemented my own AES mode with a deliberate introduced vulnerability, can you exploit my flaw to obtain the flag?

Author: ciphr
# Solution
First, by looking at the code we can see the that the only step taken to encrypt the plaintext is XORing it with the variable 'ct'. This also means that we can find that value of ct by XORing the plaintext with the ciphertext.

Let's try to encrypt a long known plaintext and print the value of 'ct' for each block. I will add a line to the encryption loop to do this, and for the plaintext, I will simply read the first 16\*32 charcters of shakespeare.txt instead of the first 16\*16 like in the original source.py.
```
# Modified shakespeare line
shakespeare = open("C:/Users/testbruker/Downloads/shakespeare.txt","rb").read()[0:16*32]

# Modified encryption loop
for i in range(0, len(plaintext), 16):
    cipher = AES.new(key, AES.MODE_CBC, iv=bytes(16))
    ct = cipher.encrypt(flag[0:12] + long_to_bytes((i//16)%16,4))
    print(ct.hex())
    ciphertext += xor(plaintext[i:i+16], ct).hex()
```
When we run the code now we get a long line of 'ct' blocks. If take a look at it, we can see that it repeats after a while. 
```
c289c5e5db20c1b6438ce67ce47a4f20 # <- First block
b0dde94915a8208cd711b76d62ddbaca
5cce41f05b68b4dadc58dbfae59cdefd
0cd602f5acee95b73b17c28b74324a42
90b2b020702c3ed59073a089bff6ccb9
927d3efcd3157ba3c3a5110843dc55c9
fa9593522f510bb46771aa01c0bda2f0
1a8135fee49790be64b7330bf1ddbdb2
d0a97609fdfd9df2dd1ba67ee80c472c
84ecf4e3ac3f4762784153c137003b0c
e8667d4721513bc0cd912b99dfe1173d
63ea9bc8b4be90e0e122304e0df37b7e
aa736c9029aa6a26599d60758eb3220c
ab0921c6099b343e0bbe1b74ec0b5c6b
52ce4a0c0356c1b75d1f8cfc0c8fbf60
5ce24015616d88f6fe0e58895c29b26a
c289c5e5db20c1b6438ce67ce47a4f20 # <- repeats here, after 256 bytes
b0dde94915a8208cd711b76d62ddbaca
5cce41f05b68b4dadc58dbfae59cdefd
0cd602f5acee95b73b17c28b74324a42
90b2b020702c3ed59073a089bff6ccb9
927d3efcd3157ba3c3a5110843dc55c9
fa9593522f510bb46771aa01c0bda2f0
1a8135fee49790be64b7330bf1ddbdb2
d0a97609fdfd9df2dd1ba67ee80c472c
84ecf4e3ac3f4762784153c137003b0c
e8667d4721513bc0cd912b99dfe1173d
63ea9bc8b4be90e0e122304e0df37b7e
aa736c9029aa6a26599d60758eb3220c
ab0921c6099b343e0bbe1b74ec0b5c6b
52ce4a0c0356c1b75d1f8cfc0c8fbf60
5ce24015616d88f6fe0e58895c29b26a
```
In the original source.py, we know that the ciphertext is prepended with 256 known characters, which is the exact amount of characters before 'ct' starts to repeat. This means that we can simply xor the flag part of the ciphertext with the exact same 'ct' as the beginning of the plaintext, which we know we can find by XORing the ciphertext with the plaintext, as mentioned earlier. Lets split the ciphertext into two variables, one containing the known text, and one containing the flag.
```
known = bytes.fromhex(cipher[:512])
flag = bytes.fromhex(cipher[512:])
```
We can use the following line to find the 'ct' used in 'known', and XOR it with 'flag'.
```
>>> print(xor(flag,xor(known,shakespeare)).decode().strip())
flag{custom_AES-CTR_with_a_reuse_vulnerability}
```
