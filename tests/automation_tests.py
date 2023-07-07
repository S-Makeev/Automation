import os
from rich.console import Console
from rich.prompt import Prompt
import shutil
import pytest

console = Console()

def make_dir(name):
    os.makedirs(f'{name}', exist_ok=True)
    console.print(f"Your [green bold]{name}[/green bold] folder has been created!")

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

def test_make_dir():
    folder_name = "test_folder"
    make_dir(folder_name)
    assert os.path.exists(folder_name)
