import os
from rich.console import Console
from rich.prompt import Prompt
import shutil
import sys

console = Console()

def make_dir(name):
  os.makedirs(f'{name}', exist_ok=True)
  


def move_deleted():
       os.makedirs('temp', exist_ok=True)
       folder_name = Prompt.ask("Enter your folder name", default="user")
       file_name = Prompt.ask("Enter your file name", default="document.txt")
       shutil.move(f"{folder_name}/{file_name}", 'temp')
    
def sort():
    temp_folder = "./temp"
    log_folder = "logs"
    mail_folder = "mail"

    os.makedirs(log_folder, exist_ok=True)
    
    os.makedirs(mail_folder, exist_ok=True)
    
    for filename in os.listdir(temp_folder):
        file_path = os.path.join(temp_folder, filename)
    
        if filename.endswith(".txt") and "log" in filename.lower():
            shutil.move(file_path, os.path.join(log_folder, filename))
    
        elif filename.endswith(".mail"):
            shutil.move(file_path, os.path.join(mail_folder, filename))

def warning():
    log_folder = "logs"
    target_folder = "parsed_logs"
    errors_log_file = "errors.log"
    warnings_log_file = "warnings.log"

    os.makedirs(target_folder, exist_ok=True)

    log_folder_path = log_folder

    errors_log_path = os.path.join(target_folder, errors_log_file)
    warnings_log_path = os.path.join(target_folder, warnings_log_file)

    with open(errors_log_path, "w") as errors_log, open(warnings_log_path, "w") as warnings_log:
    
        for filename in os.listdir(log_folder_path):
            file_path = os.path.join(log_folder_path, filename)


            with open(file_path, "r") as log_file:
                for line in log_file:
                    if "ERROR" in line.upper():
                        errors_log.write(line)
                    elif "WARNING" in line.upper():
                        warnings_log.write(line)

    shutil.move(errors_log_path, os.path.join(target_folder, errors_log_file))
    shutil.move(warnings_log_path, os.path.join(target_folder, warnings_log_file))            


def count_file_types():
    temp_folder = "./temp"

    file_types = {}
    for filename in os.listdir(temp_folder):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in file_types:
            file_types[file_extension] += 1
        else:
            file_types[file_extension] = 1

    console.print("File Type Counts:")
    for file_extension, count in file_types.items():
        console.print(f"{file_extension}: {count}")

def do_exit(message):
    sys.exit(message)


while True:
    os.system('clear')
    console.print('\n1. Create Directory\n2. Move Files\n3. Sort Files\n4. Parse Logs\n5. Count File Types\n6. Exit')
    choice = Prompt.ask('Choose a task (Enter the number)', choices=["1", "2", "3", "4", "5", "6"], default='6')

    if choice == '1':
        folder_name = Prompt.ask('Enter the folder name:')
        make_dir(folder_name)

    elif choice == '2':
        move_deleted()

    elif choice == '3':
        sort()

    elif choice == '4':
        warning()

    elif choice == '5':
        count_file_types()

    elif choice == '6':
        do_exit('Thank you for using the menu')

    else:
        console.print('Invalid choice. Please try again.')