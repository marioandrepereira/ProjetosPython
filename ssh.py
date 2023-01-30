import paramiko
import cryptocode
import random

address_list = ["", ""] # Add all the host addresses in the list
user = ""
comand = "df -h"
porta = 22

try:
    for address in address_list:
        #encrypts the entered password
        mensagem = input("Escreva a senha para acessar o host: ")
        chave = str(random.randint(123338233093093, 1023338233093093))
        MensagemCriptografada = cryptocode.encrypt(mensagem, chave)
        # create an SSH client
        client = paramiko.SSHClient()
        # automatically add the host key 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # connect to the Host
        client.connect(hostname=address, port=porta, username=user, password=cryptocode.decrypt(MensagemCriptografada, chave))

        # execute a command 
        stdin, stdout, stderr = client.exec_command(comand)

        # print the output of the command
        comandresul = stdout.readlines()
        for lin in comandresul:
            print(lin.replace("\n", ""))

        # close the SSH connection
        client.close()
except:
    print('Não foi possivel acessar o host!!')
