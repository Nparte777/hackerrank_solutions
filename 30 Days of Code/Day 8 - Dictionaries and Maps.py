if __name__=="__main__":
    n=int(input())

    phone_book=dict()
    for task in range(n):
        name, phone=input().split()
        phone_book[name]=phone


    while True:
        try:
            for query in range(n):
                query=input()
                if query not in phone_book:
                    print("Not found")
                else:
                    print("{}={}".format(query, phone_book.get(query)))
        except:
            break
