import shutil

#copyfile() -> copies contents of file
#copy() -> copyfile() + premission mode
#copy2() -> copy() + copies metadata

shutil.copyfile("test.txt", "test_copy.txt")
