import requests
import os

yn = 'y'
while yn == 'y':
    os.system('cls')
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma)")

    urls = input().split()
    for l in urls:
        l = l.strip(',')
        if '.' not in l:
            print(l, "is not valid url")
        else:
            if "https://" not in l:
                l = "https://"+l
            try:
                result = requests.get(l)
                print(l, "is up!")
            except:
                print(l, "is down!")
    while True:
        print("Do you want to start over? y/n ", end='')
        yn = input()
        if yn != 'y' and yn != 'n':
            print("That's not valid answer.")
        else:
            break

print("k.bye")
