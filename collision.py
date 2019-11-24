from pwn import *

user ='col'
host = 'pwnable.kr'
password = 'guest'
port=2222

machine = ssh(user=user, host=host, password=password, port=port)

exp = p32(0x6c5cecc) + p32(0x6c5cec8) * 4

proc = machine.process(executable='./col', argv=['col',exp])
proc.interactive()
