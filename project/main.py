import os

def GetWorkingFilePath(fileName):
    search_path = os.getcwd()
    
    # Walk through the current directory and subdirectories
    for root, dir ,files in os.walk(search_path):
        if fileName in files:
            file_path = os.path.join(root, fileName)
            print(f"File {fileName} found at: {file_path}")
            return file_path
    print(f"File {fileName} not found in {search_path}")
    return None

FileName = 'DataModelPizza.xlsx' 
path = GetWorkingFilePath(FileName)




print("test")
print(path)
