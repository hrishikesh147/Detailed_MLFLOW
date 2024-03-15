from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="Detailed_MLFLow_project"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for i in list_of_files:
    i=Path(i)

    file_dir,filename=os.path.split(i)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"created directory {file_dir} Successfully")

    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filename,"w") as f:
            pass
            logging.info(f"created emptyfile {filename} Successfully")
else:
    logging.info(f"{filename} already exists")
        

# What is the main purpose of this script?

# Answer: The script's primary purpose is to create a specific directory and file structure 
# for a machine learning project named "mlProject". If a file or directory doesn't exist, 
# it gets created.

# Why is the Path class from pathlib used, and how does it help with different operating systems?

# Answer: The Path class from pathlib provides an object-oriented interface for filesystem paths. Using Path, the script can handle file paths in a way that's compatible across different operating systems, converting slashes as appropriate (e.g., / in UNIX-like systems and \ in Windows).
# How does the script handle existing files or directories?

# Answer: If a directory or file already exists, the script does not recreate it. Specifically, the check if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0) ensures that the script only creates files that don't exist or are empty.
# What is the role of the logging module in this script?

# Answer: The logging module is used to provide feedback about the operations the script is performing, like creating directories and files. It logs messages with timestamps, which can be useful for tracking and debugging.
# Can you explain the line logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')?

# Answer: This line configures the logging settings. It sets the logging level to INFO, meaning it will capture all logging messages of level INFO and above. The format specified will display the timestamp (%(asctime)s) followed by the actual log message (%(message)s).
# What does the line os.makedirs(filedir, exist_ok=True) do, and what's the significance of exist_ok=True?

# Answer: This line creates any directories specified in the filedir variable. If the directories already exist, it won't raise an error due to the exist_ok=True parameter, ensuring the code runs smoothly without interruptions.
# Why is there an empty pass statement inside the with open(filepath, "w") as f: block?

# Answer: The pass statement is a null operation or a placeholder. In this context, it indicates that no operations are to be performed inside the file-opening block; the script merely opens the file in write mode to create it and then immediately closes it without writing anything.
# How does the code ensure that empty files are created?

# Answer: The code uses the with open(filepath, "w") as f: statement. Opening a file in write ("w") mode will create the file if it doesn't exist. Since nothing is written to the file and it's immediately closed, the result is an empty file.
# The else block at the end of the for loop logs a message indicating a file already exists. Is this behavior accurate based on the code's logic?

# Answer: No, the else block attached to a for loop runs when the loop completes without encountering a break statement. In this context, it will always run after the loop finishes, regardless of whether the last file already exists or not. The message might be misleading.
