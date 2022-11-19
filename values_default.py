import time

def print_name(name, last_name = "Sabugosa"):
    print(f"Your name is {name} {last_name}")



print_name("Rafael", "Freitas")    
print_name("Rafael")    



def connect(host, timeout=10):
    print(f"Connecting with {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("Error on connect")


connect("localhost")        