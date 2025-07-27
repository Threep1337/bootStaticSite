import re


def extract_title(markdown):
    match = re.match("# (.+)",markdown)
    if match:
        return (match.group(1).strip())
    else:
        raise Exception("No valid title found in markdown.")


def main():
    print(extract_title("# Hello"))

if __name__ == '__main__':
    main()