#!/usr/bin/python3
if __name__ == "__main__":
   from sys import argv

   ac = len(argv)
   if ac  > 1:
      i = 1
      num = 0
      for a in argv:
         if i <= ac - 1:
            num = num + int(argv[i])
            i = i + 1
      print(num)
