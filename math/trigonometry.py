"""Basic trigonometry: convert angles and compute right-triangle ratios."""
import math

angle_degrees = 30
angle_radians = math.radians(angle_degrees)

print(f"Angle: {angle_degrees} degrees = {angle_radians:.4f} radians")
print(f"sin({angle_degrees}°): {math.sin(angle_radians):.4f}")
print(f"cos({angle_degrees}°): {math.cos(angle_radians):.4f}")
print(f"tan({angle_degrees}°): {math.tan(angle_radians):.4f}")

# For a right triangle, sin(theta) = opposite / hypotenuse.
opposite = 3
hypotenuse = 5
ratio = opposite / hypotenuse
print(f"\nAngle from opposite/hypotenuse ratio: {math.degrees(math.asin(ratio)):.2f}°")
