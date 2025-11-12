from textnode import TextNode

print("hello world")
def main():
    print("This is the main function.")
    test = (TextNode("This is some anchor text", "link", "https://www.boot.dev"))
    info = repr(test)
    print(info)
main()