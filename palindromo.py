def is_palindromo(string: str) -> bool:
    string = string.replace(" ","").lower()
    # Ana # ana
    return string == string[::-1]
    # "Ana" == "anA"


def run():
    print( is_palindromo("ana"))

if __name__ == "__main__":
    run()