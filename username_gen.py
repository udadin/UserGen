import random
import string
import multiprocessing

SAVE_FILE = "usernames.txt"
NAMES_FILE = "names.txt"
PREFIX_LENGTH = 3
USERNAME_LENGTH = 10
CHARACTER_SET = string.ascii_letters + string.digits

def generate_username():
    prefix = ''.join(random.choices(string.ascii_letters, k=PREFIX_LENGTH))
    suffix = ''.join(random.choices(CHARACTER_SET, k=USERNAME_LENGTH-PREFIX_LENGTH))
    return prefix + suffix

def load_name():
    names = open('names.txt').read().splitlines()
    name =random.choice(names)
    return name

def generate_usernames(amount, prefix):
    with open(SAVE_FILE, "a") as f:
        for i in range(amount):
            if prefix is None:
                username = load_name() + generate_username()
            else:
                username = prefix + "_" + generate_username()
            f.write(username + "\n")

def generate_usernames_process(amount, prefix, num_processes):
    usernames_per_process = amount // num_processes
    processes = []
    for i in range(num_processes):
        start = i * usernames_per_process
        end = (i + 1) * usernames_per_process
        if i == num_processes - 1:
            end = amount
        p = multiprocessing.Process(target=generate_usernames, args=(end-start, prefix))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

def main():
    amount = int(input("How many usernames do you want to generate: "))
    prefix_choice = input("Do you want to use a prefix (y/n): ").lower()
    if prefix_choice == "y":
        prefix = input("What prefix do you want to use? ")
    else:
        prefix = None
    num_processes = multiprocessing.cpu_count()
    generate_usernames_process(amount, prefix, num_processes)

if __name__ == "__main__":
    main()
