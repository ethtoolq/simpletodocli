import argparse
import os

FILE = "tasks.txt" # change if needed

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


# task loader
def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]


# saving
def save(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")


# add task
def add(text):
    tasks = load()
    tasks.append("[ ] " + text)
    save(tasks)
    print(GREEN + "task added" + RESET)


# show list
def show():
    tasks = load()

    if not tasks:
        print("no tasks")
        return

    for i, t in enumerate(tasks, 1):
        if t.startswith("[x]"):
            print(GREEN + f"{i}. {t}" + RESET)
        else:
            print(f"{i}. {t}")


# check done
def done(i):
    tasks = load()

    if 1 <= i <= len(tasks):
        tasks[i-1] = tasks[i-1].replace("[ ]", "[x]")
        save(tasks)
        print(GREEN + "task complete" + RESET)
    else:
        print(RED + "wrong number" + RESET)


# remove task
def remove(i):
    tasks = load()

    if 1 <= i <= len(tasks):
        print(RED + "deleted:" + RESET, tasks[i-1])
        tasks.pop(i-1)
        save(tasks)
    else:
        print("wrong number")


parser = argparse.ArgumentParser(description="simple todo cli")
sub = parser.add_subparsers(dest="cmd")

a = sub.add_parser("add")
a.add_argument("text")

sub.add_parser("list")

d = sub.add_parser("done")
d.add_argument("id", type=int)

r = sub.add_parser("remove")
r.add_argument("id", type=int)

args = parser.parse_args()

if args.cmd == "add":
    add(args.text)

elif args.cmd == "list":
    show()

elif args.cmd == "done":
    done(args.id)

elif args.cmd == "remove":
    remove(args.id)
