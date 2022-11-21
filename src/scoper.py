
global_var = 2
local_var = 5

def hello(out=f'hello world!!!'):
    print(out)
    print(global_var + 21)
    global local_var
    local_var = 3


def main():
    print(local_var)
    hello()
    print(local_var)


if __name__=='__main__':
    main()