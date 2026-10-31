"""Explore powers, logarithms, and the change-of-base formula."""
import math

base = 2
exponent = 5
value = base**exponent

print(f"{base}^{exponent} = {value}")
print(f"log base {base} of {value} = {math.log(value, base):.1f}")
print(f"Natural log of {value} = {math.log(value):.4f}")
print(f"Common log of {value} = {math.log10(value):.4f}")

# Change of base: log_b(x) = ln(x) / ln(b).
change_of_base = math.log(value) / math.log(base)
print(f"Change-of-base result = {change_of_base:.1f}")
