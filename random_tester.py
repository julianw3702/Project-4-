from random_threads import getRand

prompt = "1"

while(prompt == "1"):
    test_range = input("How many random values do you want to test?\n")

    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(int(test_range)):
        counter[getRand()] += 1

    num = 1
    for i in counter:
        print("Number of " + str(num) + ": " +  str(i))
        num += 1
    
    prompt = input("\nIf you would like to TEST AGAIN then enter the number (1)\nIf you'd like to QUIT then enter anything\n123")
