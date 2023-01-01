def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    d_1, d_2, d_3, d_4, d_5 = n%10, n//10%10, n//100%10, n//1000%10, n//10000
    
    if d_1>=d_2 and d_1>=d_3 and d_1>=d_4 and d_1>=d_5:
        return d_1
    elif d_2>=d_1 and d_2>=d_3 and d_2>=d_4 and d_2>=d_5:
        return d_2
    elif d_3>=d_1 and d_3>=d_2 and d_3>=d_4 and d_3>=d_5:
        return d_3
    elif d_4>=d_1 and d_4>=d_2 and d_4>=d_3 and d_4>=d_5:
        return d_4
    else:
        return d_5

print(main(54035))