"""
for i in range(1, 12):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 12):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  
  print()  # Move to a new line after each row
"""

rows = 5

i = 1
while i <= rows:
  j = 1
  while j <= rows - i:
    print(" ", end="")
    j += 1

  k = 1
  while k <= (2 * i - 1):
    print("*", end="")
    k += 1

  print()
  i += 1
    