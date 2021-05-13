import os

def clear(listName=[]):
    for file in listName:
        if os.path.exists(file):
            os.remove(file)
        else:
            print("The file "+ file +" does not exist")
#clear(['0.wav', '1.wav', '2.wav', '3.wav'])