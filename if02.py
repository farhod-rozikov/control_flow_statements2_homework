def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and a<c:
        answer = a
    elif b<c and b<c:
        answer = b
    else:
        answer = c
    return answer

print(main(1,-1,0))