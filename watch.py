import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        new_pattern=re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z_0-9]+)",s)
        if new_pattern:
            final_pattern=new_pattern.groups()
            return final_pattern








if __name__ == "__main__":
    main()