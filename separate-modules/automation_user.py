# import os
# from rich.console import Console
# from rich.prompt import Prompt
# import shutil

# # Handle a deleted user.
# # user2 is a deleted user and need to move their documents from their user folder to a temporary folder. Your script will create the temporary folder. This will effectively delete the user from the system while still maintaining a record of their documents.
# def move_deleted():
#     user_input = Prompt.ask("If you want to move files, press Y/y")
#     if user_input.lower() == "y":
#        os.makedirs('temp', exist_ok=True)
#        folder_name = Prompt.ask("Enter your folder name", default="user")
#        file_name = Prompt.ask("Enter your file name", default="document.txt")
#        shutil.move(f"{folder_name}/{file_name}", 'temp')
#     else:
#         return print("You didn't enter Y/y. See you next time!")
# if __name__ == '__main__':  
#     move_deleted()