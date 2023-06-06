import subprocess
import sys
import os
import time
import random
import threading
import socket
import random
#client
def run2(command):
    try:
        subprocess.Popen(command, shell=False)
    except Exception as e:
        print("Error:", e)

def menutext2():
    colors = ["\x1b[31m", "\x1b[33m", "\x1b[34m", "\x1b[35m", "\x1b[36m", "\x1b[37m"]
    color = random.choice(colors)
    return color + """
     ░█████╗░███╗░░░███╗██████╗░██╗░░░██╗██╗   
     ██╔══██╗████╗░████║██╔══██╗╚██╗░██╔╝██║   
     ██║░░╚═╝██╔████╔██║██████╔╝░╚████╔╝░██║    
     ██║░░██╗██║╚██╔╝██║██╔═══╝░░░╚██╔╝░░██║   
     ╚█████╔╝██║░╚═╝░██║██║░░░░░░░░██║░░░██║   
     ░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝   
    """

def menu2():
    chosen_element = 0
    run2('powershell -Command "Clear-Host"')
    time.sleep(0.5)
    print(menutext2() + "\x1b[1m")

def print_menu2():
    print("┌────────────────────────┬─────────────────────────┐")
    print("│    [1]   SendMessages  │   [4]   Custom Command  │")
    print("│    [2]   Shutdown pc   │   [5]   SysInfo         │")
    print("│    [3]   End A Process │   [6]   Make file       │")
    print("└────────────────────────┴─────────────────────────┘")



    

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print('Received:', data.decode())

def send_messages(client_socket):
    while True:
        message = input("Enter a message to send or 'exit' to return to the menu: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())

def run_client(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    client_socket.connect(server_address)
    print('Connected to the server on port', port)
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    while True:
        menu2()
        print_menu2()
        choice = input("Enter your choice: ")
        if choice == '1':
            send_messages(client_socket)
        elif choice == '2':
            client_socket.sendall(b'shutdown -s -t 4 -c "noob"')
        elif choice == '3':
            print("Enter process name")
            processtoend = input("$ ")
            client_socket.sendall(b'endproc ' + processtoend.encode())
            time.sleep(2)
        elif choice == '4':
            print('enter command to send, it will run in cmd.')
            cusshell = input("$ ")
            client_socket.sendall(b'custom ' + cusshell.encode())
        elif choice == '5':
            cusshell = 'sysinfo'
            client_socket.sendall(b'custom ' + cusshell.encode())
        else:
            print("Invalid choice. Please try again.")
#server
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = random.randint(69, 42069)
    server_address = ('', port)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print('Server listening on port:', port)
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connected by {client_address}')
        while True:
            data = client_socket.recv(1024)
            decoded_data = data.decode()
            print(f'Message from {client_address}: {decoded_data}')
            if decoded_data.startswith('shutdown -s -t 4 -c "noob"'):
                run('shutdown -s -t 4 -c "noob"')
                run('powershell -Command "Clear-Host"')
                time.sleep(5)
                response = 'Shutdown command executed.'
                client_socket.sendall(response.encode())
                break
            elif decoded_data.startswith('endproc '):
                command = decoded_data[0:]
                try:
                    run(command)
                    response = f'Process "{command}" ran'
                except Exception as e:
                    response = f'Error "{command}" didnt run: {e}'
                client_socket.sendall(response.encode())
                time.sleep(2)
            elif decoded_data.startswith('custom '):
                command2 = decoded_data[7:]
                try:
                    run(command2)
                    response2 = f'Process "{command2}" ran successfully.'
                except Exception as e:
                    response2 = f'Error running "{command2}": {e}'
                client_socket.sendall(response2.encode())


#maincode
def menutext():
    colors = ["\x1b[31m", "\x1b[33m", "\x1b[34m", "\x1b[35m", "\x1b[36m", "\x1b[37m"]
    color = random.choice(colors)
    return color + """
     ░█████╗░███╗░░░███╗██████╗░██╗░░░██╗██╗   
     ██╔══██╗████╗░████║██╔══██╗╚██╗░██╔╝██║   
     ██║░░╚═╝██╔████╔██║██████╔╝░╚████╔╝░██║    
     ██║░░██╗██║╚██╔╝██║██╔═══╝░░░╚██╔╝░░██║   
     ╚█████╔╝██║░╚═╝░██║██║░░░░░░░░██║░░░██║   
     ░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝   
    """
def run(command):
    try:
        subprocess.Popen(command, shell=False)
    except Exception as e:
        print("Error:", e)

def end_process(process_name):
    try:
        subprocess.Popen(["taskkill", "/F", "/IM", process_name], shell=False)
    except Exception as e:
        print("Error:", e)

def open_process(process_name):
    try:
        subprocess.Popen(process_name, shell=False)
    except Exception as e:
        print("Error:", e)

def bully():
    try:
        run("notepad.exe")
        run("explorer.exe")
        time.sleep(0.1)
    except Exception as e:
        print("Error:", e)

def slow_text_appear(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

def menu():
    chosen_element = 0
    run('powershell -Command "Clear-Host"')
    time.sleep(0.5)
    print(menutext() + "\x1b[1m")

    def print_menu():
        print("┌────────────────────────┬─────────────────────────┬─────────────────────────┐")
        print("│    [1]   Shutdown -s   │   [7]   Custom Shell    │   [12]  StartChatServer │")
        print("│    [2]   Shutdown -i   │   [8]   SysInfo         │   [13]  StartChatPeer   │")
        print("│    [3]   End A Process │   [9]   Make File       │   [14]  wp              │")
        print("│    [4]   Bully PC      │   [0]   Exit            │   [15]  wp              │")
        print("│    [5]   Crash         │   [10]  Start Proc      │   [16]  wp              │")
        print("│    [6]   Max Vol       │   [11]  MSG             │   [17]  wp              │")
        print("└────────────────────────┴─────────────────────────┴─────────────────────────┘")

    print_menu()
    chosen_element = input("$ ")

    try:
        if int(chosen_element) == 1:
            run('shutdown -s -t 4 -c "noob"')
            run('powershell -Command "Clear-Host"')
            time.sleep(3)
            menu()
        elif int(chosen_element) == 2:
            run("shutdown -i")
            run('powershell -Command "Clear-Host"')
            time.sleep(1)
            menu()
        elif int(chosen_element) == 3:
            print("Enter Process Name.")
            procname = input("$ ")
            end_process(procname)
            run('powershell -Command "Clear-Host"')
            time.sleep(1)
            menu()
        elif int(chosen_element) == 4:
            i = 1
            while i == 1:
                bully()
            text = "................................................................................................................................................................................................"
            delay = 0.8
            print("Bullying", end="")
            slow_text_appear(text, delay)
            time.sleep(120)
        elif int(chosen_element) == 5:
            end_process('Explorer')
            end_process('')
        elif int(chosen_element) == 6:
            j = 1
            while j < 100:
                run(
                    'powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]175)"'
                )
        elif int(chosen_element) == 7:
            customrun = input("$ ")
            run(customrun)
            run('powershell -Command "Clear-Host"')
            time.sleep(0.5)
            menu()
        elif int(chosen_element) == 8:
            run('powershell -Command "systeminfo"')
            time.sleep(5)
            menu()
        elif int(chosen_element) == 9:
            username = os.getlogin()
            filename = input("Enter file name $ ")
            texts = "idk"
            run(
                'powershell -Command "cd C:\\Users\\'
                + username
                + "\\Desktop ; echo "
                + texts
                + " > "
                + filename
                + '"'
            )
            print("Wrote File: " + filename)
            run('powershell -Command "Clear-Host"')
            time.sleep(1)
            menu()
        elif int(chosen_element) == 10:
            print("Enter Process Name.")
            procname = input("$ ")
            open_process(procname)
            run('powershell -Command "Clear-Host"')
            time.sleep(1)
            menu()
        elif int(chosen_element) == 11:
            print("hi")
        elif int(chosen_element) == 12:
            run_server()
        elif int(chosen_element) == 13:
            port = int(input("Input port, it's shown by the server when starting ConMe: "))
            run_client(port)
        elif int(chosen_element) == 0:
            sys.exit()
        else:
            print("incorrect choice.")
            time.sleep(0.1)
            run('powershell -Command "Clear-Host"')
            time.sleep(0.1)
            menu()
    except ValueError:
        print("Please enter a valid menu option.")
        time.sleep(0.1)
        run('powershell -Command "Clear-Host"')
        time.sleep(0.5)
        menu()
    except Exception as e:
        print("Error:", e)
        time.sleep(1)
        run('powershell -Command "Clear-Host"')
        time.sleep(0.5)
        menu()




if __name__ == "__main__":
    """Python script main function"""
    menu()
