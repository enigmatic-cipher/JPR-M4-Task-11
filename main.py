"""
A statement is a string of words where each word is separated by a space. Count the number of words in the string and create a new string consisting of each word is along with its length.
Input-> "A cat ran down the lane"
Output-> Number of words = 6 | A:1 cat:3 ran:3 down:4 the:3
"""

st = "A cat ran down the lane"
ln = len(st.split())
print(f"Number of Words: {ln}")
for i in range(0,ln):
  ch = st.split()
  e = ch[i]
  ln_2 = len(e)
  print(f"{e}:{ln_2}")
