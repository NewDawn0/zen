# Only used for the cs50 subission form
# Does not actually do anything



from zen.main import main

class Three():
    def __init__(self):
        pass

# 3 random functions are required
def one() -> int:
    return 5
def two() -> str:
    return "Hello World"
def three() -> Three:
    return Three()

if __name__ == "__main__":
    one()
    two()
    three()
    main()
