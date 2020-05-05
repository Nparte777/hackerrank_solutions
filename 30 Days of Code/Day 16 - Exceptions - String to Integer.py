#!/bin/python3

import sys
S = input().strip()
try:
    S=int(S)
    print(S)

except:
    print("Bad String")

'''C++ Code Alternative'''
# int main(){
#     std::string S;
#     cin >> S;
#     try{
#         cout<<stoi(S);
#     }
#      catch(exception e)
#      {
# cout<<"Bad String";
#      }
#     return 0;
# }
