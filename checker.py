import os
file_path = "collected_reddits_1.csv"
file_size = os.path.getsize(file_path)
file_size = file_size/1024/1024
print(f"The size of {file_path} is {file_size} MB")