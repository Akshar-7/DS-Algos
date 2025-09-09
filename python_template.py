from sys import stdin
input = stdin.readline
def main():
  n = int(input())
  n,q = map(int, input().split())
  a = [int(i) for i in input().split()]
  #b = [int(i) for i in input().split()]
  #c = [int(i) for i in input().split()]
  #c = [list(i) for i in input().split()]
  #b = [int(i) for i in input().split()]
  #s = input()
  

t = int(input())
for __ in range(t):
  print(main())
