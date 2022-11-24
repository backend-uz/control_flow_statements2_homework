def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if temp==0:
        return "Freezing"
    if temp <= 10:
        return "Very cold"
    if temp <= 20:
        return "Cold"
    if temp <= 30:
        return "Normal"
    if temp <=39:
        return "Hot"
    if temp == 40:
        return "Very hot"
print(main(38))