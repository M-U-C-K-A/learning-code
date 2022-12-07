import random
import time
import socket
import struct
import names
import secrets
from faker import Faker


Faker.seed(0)
fake = Faker(['fr_FR'])

loading =("■▢▢▢▢▢▢▢▢▢ 10% ","■■▢▢▢▢▢▢▢▢ 20% ","■■■▢▢▢▢▢▢▢ 30% ","■■■■▢▢▢▢▢▢ 40% ","■■■■■▢▢▢▢▢ 50% ","■■■■■■▢▢▢▢ 60% ","■■■■■■■▢▢▢ 70% ","■■■■■■■■▢▢ 80% ","■■■■■■■■■▢ 90% ","■■■■■■■■■■ 100%")
for i in range(10):
    print(loading[i])
    time.sleep(random.randint(20,90)/1000)
print('username : ✅')
print('password : ✅')
time.sleep(.2)
print('--------------')
print('successful authentication')
print('--------------')
time.sleep(.2)
for _ in range(50):
    ip=socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    print('\n-----',names.get_full_name(),'-----')
    print(fake.address(),'\n')
    print('heure du hack :',fake.time())
    print('Email :',fake.ascii_email(),'\nPassword :',secrets.token_urlsafe(5),'\nUsername : ',fake.user_name(),'\n')
    print('Plaque d\'imatriculation : ',fake.license_plate())
    print('Iban : ',fake.iban())
    print('adresse IPV4 :',ip)
    #print(fake.catch_phrase())
    time.sleep(.2)
