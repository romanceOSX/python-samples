import subprocess

def print_elements(list):
    for e in list:
        print(e);

def main():
    args = [
            "ls",
            "-alh",
            ]
    ret = subprocess.run(args,
                         capture_output=True,
                         );
    print("stderr: ", ret.stderr)

    print("stdout: ")
    print_elements(str(ret.stdout).split('\\n'))

if __name__ == "__main__":
    main()

