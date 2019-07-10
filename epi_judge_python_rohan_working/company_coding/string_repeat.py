from heapq import *
from collections import Counter

def rearrange_string(str):
  # TODO: Write your code here
  if str == '':
    return ''
  count_str = Counter(str)
  max_heap = []
  distict_word = 0
  for word, freqency in count_str.items():
    heappush(max_heap, (-freqency, word))


  prev_word, prev_freq = None, 0
  result = []
  while max_heap:
    freqency, word = heappop(max_heap)
    if prev_word and -prev_freq > 0:
      heappush(max_heap, (prev_freq, prev_word))
    result.append(word)
    prev_freq = freqency + 1
    prev_word = word
#  print(result)
  return "".join(result) if len(result) == len(str) else ""





  return ""


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()
