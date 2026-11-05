def num_split(num):
  return [int("".join([f"-{str(num)[x]}" if num < 0 else str(num)[x]]+["0" for _ in range(0,len(str(num))-1-x)])) for x in range(*[1,len(str(num))] if num < 0 else [len(str(num))])]
print(num_split(-123))