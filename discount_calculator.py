def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    A discount is applied only if it is 20% or higher.
    
    :param price: Original price of the item (float)
    :param discount_percent: Discount percentage (float)
    :return: Final price after discount (float)
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Prompt user for inputs
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if final_price == original_price:
    print(f"No discount applied. The original price remains: ${final_price:.2f}")
else:
    print(f"Discount applied! The final price after {discount_percentage}% discount is: ${final_price:.2f}")
