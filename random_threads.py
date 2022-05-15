from threading import Thread

def getRand():
    thread = Thread()
    thread.start()
    randInt = thread.native_id % 13 #+ 1
    # print(thread.native_id)
    thread.join()
    return randInt

if __name__ == "__main__":
    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1300000000):
        counter[getRand()] += 1
    
    num = 1
    for i in counter:
        print("Number of " + str(num) + ": " +  str(i))
        num += 1