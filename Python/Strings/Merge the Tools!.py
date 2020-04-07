def merge_the_tools(string, k):
    while string:
        result = ""
        str_chunck = string[:k]
        string = string[k:]         #Recursive
        for ele in str_chunck:
            if ele not in result:
                result += ele
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
