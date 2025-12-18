from mark_to_html import markdown_to_html_node
import os
import shutil

def main():
    # Copy content from the static directory to the public directory
    copy_directory(src="static", dest="public")
    # Generate content for the website using the from, template, and destination paths
    generate_page(from_path="content/index.md", template_path="template.html", dest_path="public/index.html")
    print("halt operation with 'Ctrl + z'")

# create a recursive function to copy all contents from a 
# source directory to a destination directory
def copy_directory(src, dest):
    # the file paths are relative to the current working directory
    # First, delete contents of destination directory if it exists
    if os.path.exists(dest):
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

# pull the h1 header from a markdown string (line starts with a single #)
# if no h1 header is found, raise exception
def extract_title(markdown):
    lines = markdown.split("\n")
    lines = [line.strip() for line in lines if line.strip() != '']

    if lines and lines[0].startswith("# "):
        return lines[0].lstrip("# ")
    else:
        raise Exception("No h1 header found in markdown")
    
def generate_page(from_path, template_path, dest_path):
    # print a message indicating the start of page generation
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read from_path markdown file. Store content in a variable.
    with open(from_path) as file:
        content = file.read()
    
    # read template_path file. Store content in a variable.
    with open(template_path) as file:
        template = file.read()

    # use markdown_to_html function and .to_html() method 
    # convert the markdown content to html
    html_content = markdown_to_html_node(content).to_html()

    # use extract_title function to get the title
    title = extract_title(content)

    # replace {{title}} and {{content}} placeholders in template with title and html content
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # write the new full HTML
    with open(dest_path, "w") as file:
        file.write(template)


# Call the main function
main()