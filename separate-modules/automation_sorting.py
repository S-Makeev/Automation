# import os
# from rich.console import Console
# from rich.prompt import Prompt
# import shutil

# def sort():
#     temp_folder = "./temp"
#     log_folder = "logs"
#     mail_folder = "mail"

#     os.makedirs(log_folder, exist_ok=True)

#     os.makedirs(mail_folder, exist_ok=True)

#     for filename in os.listdir(temp_folder):
#         file_path = os.path.join(temp_folder, filename)

#         if filename.endswith(".txt") and "log" in filename.lower():
#             shutil.move(file_path, os.path.join(log_folder, filename))

#         elif filename.endswith(".mail"):
#             shutil.move(file_path, os.path.join(mail_folder, filename))