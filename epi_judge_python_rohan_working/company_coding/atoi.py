def myAtoi(str: str) -> int:
    str = str.strip()
    print(str)
    numeric = [char for char in str.strip() if len(char) > 0]
    # for char in str:
    #     if char == "-"  or char.isdigit() and char != "":
    #         numeric.append(char)

    if numeric[0] == '-':
        return int("".join(numeric[1:])) * -1
    else:
        return int("".join(numeric))

def main():
    print(myAtoi("   -42"))


main()
