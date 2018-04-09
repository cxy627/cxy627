def safe_sqrt(invalue):
    import math
    try:
        result= math.sqrt(invalue)
    except ValueError:
        result = math.sqrt(-invalue)
    return result
