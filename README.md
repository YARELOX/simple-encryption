# How to make a key.
A key must be a string, consisting of alternating colons and numbers.
Example of a key: '50:40:2:3:10:6'
Key can be as long as you want, but there is one rule, not following which you won't be able to decrypt encrypted text:
<<<<<<< HEAD
check if you can decrypt text after encrypting it, some keys(most of them are not divisible by 10(except number < 10)) make text undecryptable. This is a bug I can't fix at the moment.
=======
every number more than 10 must be divisible by 10. This is a bug, which I can't fix at the moment.
>>>>>>> 8c5f9f1035270b4bb64413ccced944520602f737
