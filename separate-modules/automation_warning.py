# import os
# import shutil

# def warning():
#   log_folder = "logs"
#   target_folder = "parsed_logs"
#   errors_log_file = "errors.log"
#   warnings_log_file = "warnings.log"

#   os.makedirs(target_folder, exist_ok=True)

#   log_folder_path = log_folder

#   errors_log_path = os.path.join(target_folder, errors_log_file)
#   warnings_log_path = os.path.join(target_folder, warnings_log_file)

#   with open(errors_log_path, "w") as errors_log, open(warnings_log_path, "w") as warnings_log:

#       for filename in os.listdir(log_folder_path):
#           file_path = os.path.join(log_folder_path, filename)


#           with open(file_path, "r") as log_file:
#               for line in log_file:
#                   if "ERROR" in line.upper():
#                       errors_log.write(line)
#                   elif "WARNING" in line.upper():
#                       warnings_log.write(line)

#   shutil.move(errors_log_path, os.path.join(target_folder, errors_log_file))
#   shutil.move(warnings_log_path, os.path.join(target_folder, warnings_log_file))
