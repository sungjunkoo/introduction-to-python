"""
Numeric Data Types and Their Operators
- Author: Sungjun Koo
- Date: August 28, 2025
- Purpose: This file demonstrates concepts and syntax from an online lecture.
"""

# ========================================
# Numeric Data Types
# ========================================

# Integer (정수형)
# Integers are whole numbers, positive or negative.
a = 123
a = -178
a = 0

# Floating Point (실수형)
# Floating-point numbers have decimal points.
a = 1.2
a = -3.45

# E notation (컴퓨터식 지수 표현 방식)
# E notation represents powers of 10.
a = 4.24E10 # 4.24 * 10^10
a = 4.24e-10 # 4.24 * 10^-10

# Octal (8진수) and Hexadecimal (16진수)
# These are different number systems used to represent integers.
octal_num = 0o177 # Octal number for 127
hex_num = 0xABC # Hexadecimal number for 2748
# 0o177 = 1 * 8^2 + 7 * 8^1 + 7 = 127
# 0xABC = 10 * 16^2 + 11 * 16^1 + 12 = 2748


# ========================================
# Numeric operators
# ========================================

# Elementary Arithmetic (사칙연산)
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Exponentiation (거듭제곱)
# Raises the first number to the power of the second number.
print(3 ** 4) # 3의 4제곱

# Modulo (나머지)
# Returns the remainder of a division.
print(7 % 3) # 7을 3으로 나눈 나머지

# Floor Division (몫)
# Returns the integer part of a divsion result.
print(7 // 3) # 7을 3으로 나눈 몫