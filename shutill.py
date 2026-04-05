import shutil

# Copy a file from one location to another
shutil.copy("file1.txt", "file2.txt")
print("File copied successfully!")

# Move a file
# shutil.move("destination.txt", "backup/destination.txt")
# print("File moved successfully!")
#
# # Make an archive (zip folder)
# shutil.make_archive("my_backup", "zip", "backup")
# print("Backup created successfully!")
#
# # Remove a directory tree
# shutil.rmtree("backup")
# print("Backup folder deleted!")
