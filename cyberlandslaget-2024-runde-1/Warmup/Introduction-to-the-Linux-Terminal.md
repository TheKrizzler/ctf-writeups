# Challenge
>You will be given the IP address and port number of a remote host.
>
>Your first step is to connect to the Linux server using SSH.
>
>From there you need to use basic command line tools to find a password that unlocks the next level.
>
>There are a total of 10 levels and each one requires different tricks to find the password.

Author: iLoop, nordbo
# Solution
### Level 1
```
$ cat readme
The password for level2 is 9566788fb63a0bd391fe51cf9ee57e05
```
This command displays the contents of the readme file, which gives us the password to the next level.
### Level 2
```
ls -al
```
This command reveals hidden folders and files. Run 'cat' on it to reveal the password.
```
$ cat .secret
c879e02a29f5487da2578899d9c1f4ba
```
### Level 3
In this level the file containing the password has a strange filename containing abnormal characters. This means that we can't run 'cat' like we normally would.

Instead I will run the following command:
```
$ cat -- '- ~ password for next level!.txt'
7e54d6ad4ec112760a797276b8c720df
```
### Level 4
In this challenge we don't have permissions to read the file, but we have the power to change permissions. One solution is to use the following command:
```
$ chmod 777 level_5_password
$ cat level_5_password
fafb4d7766fb36ccb6083cc05ff536ff
```
### Level 5
In this challenge, we simply need to run the executable on the password file instead of the regular cat command.
```
./supercat password.txt
e7c73221b5e6177e105c312cf9410153
```
### Level 6
In this challenge we have a large folder system in which the password file is hiding. We don't know what the file is called, but I assume it ends with '.txt'.
```
find . | grep .txt
```
This reveals a single file.
```
$ find . | grep .txt
./my_files/zamajqa/ylnbxqhb/password_next_level.txt

$ cat my_files/zamajqa/ylnbxqhb/password_next_level.txt
ea4100c819acef5fde77fb5a5a5d5e05
```
### Level 7
In this challenge we get a large .json file containing a lot of information. By running 'cat' on it we can see that almost every single "password" line contains the value "dummy". First we have can use grep to fiter out every line that doesn't contain "password", then a grep with the inverse option to filter out every line that contains "dummy".
```
cat config.json | grep password | grep -v dummy

"password": "7d591d9caf654ab0c9288f45648982ef",
```
### Level 8
In this challenge we get a long list of passwords, and need to find the password two lines above a given password. First we can use '-n' to get line numbers when we read the file. Then grep to find the password specified in the readme.
```
$ cat -n passwords.txt | grep 1c778041d48203055e30a7c3604b7479
5897	1c778041d48203055e30a7c3604b7479
```
Now that we have the line number, we can simply look for the line number 5895.
```
$ cat -n passwords.txt | grep 5895
5895	6983b1017316eab84327c94ab74232e9
10098	018a1b6ccd2ec81361657e259155895a
10490	9271858951e6fe9504d1f05ae8576001
11563	658953f1f681915f543a40eef9acb562
```
This gives multiple matches, but we can clearly see that the first one matches the line number.
### Level 9
In this challenge we can run the following command to find files owned by 'level10':
```
$ find . -user level10
./files/igloejkx
$ cat files/igloejkx
c65e8c3fcf9653f05f53574374027b26
```
### Level 10
Since the file size in provided in hex as 0x1337, we need to convert it to decimal first, which becomes 4919. We can run the following command to filter files by size:
```
find / -size 4919c
```
This gives us a bunch of files but one stands out, and it's the only one that isn't followed by "Permission denied" or something similar.
```
/usr/lib/x86_64-linux-gnu/perl/cross-config-5.34.0/config.txt
```
When we run 'cat' on this file we can see that it contains a long base64 encoded string, so let's run the following command to find the flag:
```
$ cat /usr/lib/x86_64-linux-gnu/perl/cross-config-5.34.0/config.txt | base64 -d | grep flag
flag{m4st3r_0f_c0mmand_l1n3_m4g1c}
```