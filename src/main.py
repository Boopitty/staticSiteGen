from textnode import TextNode
import os
import shutil

def main():
    # Create a TextNode instance and print its representation
    test = (TextNode("This is some anchor text", "link", "https://www.boot.dev"))
    info = repr(test)
    print(info)
    copy_directory()

# create a recursive function to copy all contents from a 
# source directory to a destination directory
def copy_directory(src="static", dest="public"):
    # the file paths are relative to the current working directory
    # First, delete contents of destination directory if it exists
    if os.path.exists(dest) and dest.endswith("public"):
        shutil.rmtree(dest)
        os.makedirs(dest)

    # Now copy contents from source to destination
    if os.path.exists(src):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            if os.path.isdir(s):
                # create the directory in destination if it doesn't exist
                if not os.path.exists(d):
                    os.mkdir(d)
                # recursive call to copy the contents of the directory
                copy_directory(s, d)
            else:
                # copy the file to the destination
                shutil.copy2(s, d)

# Call the main function
main()