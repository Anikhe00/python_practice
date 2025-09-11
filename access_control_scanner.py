# 🛂 Access Control Scanner Challenge

# 1. Create a set of revoked badge numbers.
revoked_badge_numbers = {"OS5212", "OS6215", "OS7821", "OS8912", "OS2512"}

# 2. Create two empty lists: "approved" and "denied".
approved = []
denied = []

# 3. Start a loop to collect visitor info:
while True:
  # - Ask for the visitor's name (or type "done" to finish).
  name = input("Enter your name (or type 'done' to finish): ")

  # - If the name is "done", exit the loop.
  if name.lower() == "done":
    break

  # - Otherwise, ask for their badge number.
  else:
    badge_number = input("Enter badge number: ").strip().upper()

    # - Check if the badge is revoked:
    # - If revoked: add the name to "denied" and display "ACCESS DENIED".
    if badge_number in revoked_badge_numbers:
      denied.append(name)
      print("ACCESS DENIED")

    # If not: add the name to "approved" and display "ACCESS GRANTED".
    else:
      approved.append(name)
      print("ACCESS GRANTED")

# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":

# - Sort both lists alphabetically.
sorted_approved = sorted(approved)
sorted_denied = sorted(denied)

# - Display the total number of approved and denied visitors.
print("✅ Approved List")
for num, approved in enumerate(sorted_approved, 1):
  print(num, approved)

print("⛔️ Denied List")
for num, denied in enumerate(sorted_denied, 1):
  print(num, denied)

print(f"Total approved visitors: {len(sorted_approved)}")
print(f"Total denied visitors: {len(sorted_denied)}")