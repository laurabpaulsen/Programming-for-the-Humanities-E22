from scoper import hello
import random

def main():
    hello(out=f'hello universe!!!')
    print(random.randint(1,4))

if __name__=='__main__':
    main()