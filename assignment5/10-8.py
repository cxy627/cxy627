def safe_input():
    try:
        result = input()
    except (EOFError,KeyboardInterrupt):
        return None
    else:
        return result
