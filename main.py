from pathlib import Path
import os

def createfile():
    try:
        name = input("enter the name of file you want to create")
        path = Path(name)
        if not path.exists():
            with open(name,"w") as f:
                data = input("what do you want to write inside your file:")
                f.write(data)
            print("File created successfully")
        else:
            print("ERROR  File already exists")
    except Exception as err:
         print(f"An error occured as {err}")
def readfile():
    try:
        name = input("Enter File name:")
        path = Path(name)
        if path.exists():
            with open(name,"r") as f:
                data = f.read()
                print(f"The content of your file is:\n {data}")
        else:
            print("File does not exist \n create a file first")
    except Exception as err:
        print(f"An error occured as {err}")
def upadtefile(): 
    try:
        name = input("Enter File name:")
        path = Path(name)
        if path.exists():
            print("YOU CAN PERFORM FOLLOWING OPERATIONS")
            print("1.Rename the file")
            print("2.Append the content")
            print("3.overwrite the content")

        choice = int(input("Enter your choice"))
        if choice == 1:
            newname = input("Enter a new name for file:")
            new_path = Path(newname)
            if new_path.exists():
                path.rename(new_path)
                print("file renamed successfully")
            else:
                print("File already exists")

        elif choice == 2:
            if path.exists():
                with open(name,"a") as f:
                    data = input("What do you want to append?:")
                    f.write("\n"+data)
        elif choice == 3: 
            if path.exists():
                with open(name,"w") as f:
                    data = input("What do you want to overwrite?:")
                    f.write(data)
    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        name = input("Enter File name:")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("File deleted successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error occured as {err}")




print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")


user_response = int(input("\n Enter your response"))


if user_response == 1:
    createfile()
elif user_response == 2:
    readfile()
elif user_response == 3:
    upadtefile()
elif user_response == 4:
    deletefile()
