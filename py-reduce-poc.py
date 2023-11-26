from functools import reduce

#tags = ["hi nanna", "hi naana", "hi nanna"]
tags = []

def form_hashtags(prev, curr):
  print(f"Prev: {prev}")
  print(f"Curr: {curr}")
 
  return f"{prev} #{curr.strip().title().replace(' ', '')}"

hash_tags = reduce(lambda prev, curr: f"{prev} #{curr.strip().title().replace(' ', '')}", tags,"")
#hash_tags = reduce(form_hashtags, tags,"")
print(hash_tags)