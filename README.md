# Simple To-Do CLI

A simple terminal task manager written in Python.

The program allows adding tasks, viewing the task list, marking tasks as done, and removing tasks.

## Features

    add tasks
    view task list
    mark tasks as done
    remove tasks

Tasks are saved to a text file.

## Requirements

    Python 3

## Usage

Run the program:


```
python3 todo.py

```
Add a task


```
python3 todo.py add "buy milk"

```
### Show task list


```
python3 todo.py list

```
## Example output:


```
1. [ ] buy milk
2. [ ] do homework
3. [x] read a book

```
### Mark a task as done


```
python3 todo.py done 1

```
### Remove a task


```
python3 todo.py remove 2

```
### How the program works

All tasks are saved in a file:

tasks.txt

### Example file contents:


```
[ ] buy milk
[x] finish project
[ ] read a book

```
## Project purpose

This project was created for practice:

    Python basics
    working with argparse
    working with files
    creating CLI programs

## License

MIT
