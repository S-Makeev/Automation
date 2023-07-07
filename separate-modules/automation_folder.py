# import os
# from rich.console import Console
# from rich.prompt import Prompt

# console = Console()

# def make_dir():
#   name = Prompt.ask("Enter your folder name", default="user2")
#   os.makedirs(f'{name}', exist_ok=True)
#   with open(f'{name}/user2.txt', 'w') as f:
#       f.write('This is my new file')
#       console.print(f"Your [green bold]{name}[/green bold] folder has been created!")


# if __name__ == '__main__':
   
#    make_dir(folder_name)