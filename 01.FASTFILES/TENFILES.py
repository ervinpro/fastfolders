import os

for i in range(1, 3):
    folder_name = f"Folder_{i}"
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")