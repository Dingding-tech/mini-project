from utils import ppap,jet_2
import time

def run():
    time.sleep(1)
    a = input("Which effect do you want? 1 or 2 ?")
    if a == "1":
        ppap()
    elif a == "2":
        jet_2()
    else:
        print("Not an available command! ")

if __name__ == "__main__" :
    try:
        run()
    except Exception as e:
        print("Error encountered: {}".format(e))

