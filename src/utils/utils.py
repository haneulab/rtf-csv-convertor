import sys

from typing import Callable
from time import sleep
def debug(module_name: str = __name__, debugger : Callable[[str], None] = None, flag : str = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1] if len(sys.argv) > 1 else "") -> None:
    if not module_name:
        return None
    if not debugger:
        return None
    if module_name == "__main__":
        if flag in ("-b", "--build"):
            print("building...")
            sleep(0.25)
            print(".")
            print(".")
            sleep(0.25)
            print(".")
            print(".")
            print(".")
            sleep(0.55)
            print("successfully built!")
            return None
        if flag:
            print(f"'{flag}' is an unkown flag. Please use one of the following flags listed below.")
            print("\t-t | --test : This flag runs program unittest.")
            print("\t-b | --build : This flag builds final package.")
            return None
        debugger(module_name)
    return None
