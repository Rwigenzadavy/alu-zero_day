# create_hello.py

# This script creates a file called 'hello.py' and writes "hi hi hi" into it

def main():
    with open("hello.py", "w") as f:
        f.write("hi hi hi\n")

    print("hello.py created with content: hi hi hi")

if __name__ == "__main__":
    main()

