# ☕️ Loyalty Points Engine Challenge

# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold

# STEPS:
purchases = [3.75, 7.20, 2.50, 4.45]

# 1. Define earn_points(price) → returns points for one purchase
def earn_points(price):
    """
    Convert the purchase amount into whole amount.
    Each whole dollar = 3 points
    Calculate the number of points per whole dollar
    """
    whole_dollar = int(price)
    points = whole_dollar * 3
    return points
    
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
def tier_label(points):
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Bronze"
    else:
        return "Silver"
        
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
total_points = 0
total_spent = 0.0

for purchase in purchases:
    points = earn_points(purchase)
    total_points += points
    total_spent += purchase

    
# 4. After the loop, call tier_label(total_points)
final_tier = tier_label(total_points)

# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

print("---- Loyalty Summary ----")
print(f"Total dollars spent: ${total_spent: .2f}")
print(f"Total points earned: {total_points}")
print(f"Final tier: {final_tier}")

