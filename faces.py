def convert(str):
    str = str.replace(':)', '🙂')
    str = str.replace(':(', '🙁')
    return(str)

def main():
    string = input('input: ')
    print(convert(string))

main()