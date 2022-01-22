def isBetterDeal():
    uncle = 1000000
    father = 0.01
    for i in range(30):
        uncle = uncle - father
        father = father * 2
    return uncle

def main():
    s = isBetterDeal()
    print(s)
    print('s')

if __name__ == '__main__':
    # Do not change this part
    main()
