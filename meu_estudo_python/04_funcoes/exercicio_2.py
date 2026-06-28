def media(*args):
    return sum(args) / len(args)

print(f"A média é: {media(10, 7, 8):.2f}")