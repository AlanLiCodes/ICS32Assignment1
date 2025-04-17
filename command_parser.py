# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME
# EMAIL
# STUDENT ID

import shlex
from pathlib import Path
from notebook import Notebook, Diary

class CommandParser:
    def __init__(self):
        self.notebook_obj = None
        self.notebook_path = None

    def parse_and_execute(self,command: str) -> None:
        raw_tokens = shlex.split(command)
        tokens = [t.strip() for t in raw_tokens]
        if not tokens:
            print("ERROR")
            return
        cmd = tokens[0].upper()
        args = tokens[1:]

        if cmd == 'C':
            self.handle_create(args)
        elif cmd == 'D':
            self.handle_delete(args)
        elif cmd == 'O':
            self.handle_open(args)
        elif cmd == 'E':
            self.handle_edit(args)
        elif cmd == 'P':
            self.handle_print(args)
        else:
            print("ERROR")

    def handle_create(self, args: list[str]) -> None:
        if '-n' not in args or len(args) < 3:
            print("ERROR")
            return
        try:
            name_index = args.index('-n')
            path = Path(args[0]).expanduser().resolve()
            diary_name = args[name_index + 1]
            full_path = path / f"{diary_name}.json"

            if not path.exists() or full_path.exists():
                print("ERROR")
                return

            username = input("")
            password = input("")
            bio = input("")

            nb = Notebook(username, password, bio)
            nb.save(full_path)

            print(f"{full_path} CREATED")
        except Exception:
            print("ERROR")


    def handle_delete(self,args: list[str]) -> None:
        try:
            path = Path(args[0]).expanduser().resolve()
            if not path.exists() or path.suffix != '.json':
                print("ERROR")
                return
            path.unlink()
            print(f"{path} DELETED")
        except Exception:
            print("ERROR")

    def handle_open(self,args: list[str]) -> None:
        try:
            path = Path(args[0]).expanduser().resolve()
            if not path.exists() or path.suffix != '.json':
                print("ERROR")
                return
            username = input("")
            password = input("")

            nb = Notebook("", "", "")
            nb.load(path)

            if nb.username == username and nb.password == password:
                self.notebook_obj = nb
                self.notebook_path = path
                print("Notebook loaded.")
                print(nb.username)
                print(nb.bio)
            else:
                print("ERROR")
        except Exception:
            print("ERROR")

    def handle_edit(self, args: list[str]) -> None:
        if self.notebook_obj is None or self.notebook_path is None:
            print("ERROR")
            return
        try:
            i = 0
            while i < len(args):
                option = args[i]
                if option == '-usr':
                    self.notebook_obj.username = args[i + 1]
                    i += 2
                elif option == '-pwd':
                    self.notebook_obj.password = args[i + 1]
                    i += 2
                elif option == '-bio':
                    self.notebook_obj.bio = args[i + 1]
                    i += 2
                elif option == '-add':
                    self.notebook_obj.add_diary(Diary(args[i + 1]))
                    i += 2
                elif option == '-del':
                    if not self.notebook_obj.del_diary(int(args[i + 1])):
                        print("ERROR")
                        return
                    i += 2
                else:
                    print("ERROR")
                    return
                self.notebook_obj.save(self.notebook_path)
        except Exception:
            print("ERROR")

    def handle_print(self,args: list[str]) -> None:
        if self.notebook_obj is None or self.notebook_path is None:
            print("ERROR")
            return
        try:
            i = 0
            while i < len(args):
                option = args[i]
                if option == '-usr':
                    print(self.notebook_obj.username)
                elif option == '-pwd':
                    print(self.notebook_obj.password)
                elif option == '-bio':
                    print(self.notebook_obj.bio)
                elif option == '-diaries':
                    for i, entry in enumerate(self.notebook_obj.get_diaries()):
                        print(f"{i}: {entry.entry}")
                elif option == '-diary':
                    idx = int(args[i + 1])
                    print(self.notebook_obj.get_diaries()[idx].entry)
                    i += 1
                elif option == '-all':
                    print(self.notebook_obj.username)
                    print(self.notebook_obj.password)
                    print(self.notebook_obj.bio)
                    for i, entry in enumerate(self.notebook_obj.get_diaries()):
                        print(f"{i}: {entry.entry}")
                else:
                    print("ERROR")
                    return
                i += 1
        except Exception:
            print("ERROR")
