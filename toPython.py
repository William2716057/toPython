import os

def rename_files(directory, suffix):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            base = os.path.splitext(filename)[0]
            new_name = base + suffix
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print("Text files changed to Python files")

#uncomment either 
#directory_path = os.getcwd()
#directory_path = 'your_directory_path_here'
suffix = '.py' 
rename_files(directory_path, suffix)