
from calculator import square
import pytest

### unit testing manual way

# def main():
#     test_square()


# def test_square():
#     # way 1
    
    
#     # assert square(2) == 4
#     # assert square(3) == 9
#     # assert to make sure whether its true(simpler than if else)


#     # way 2
    
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
    
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
        
        

# # follow the convention now on
# if __name__ == "__main__":
#     main()



### unit testing with pytest
### no function run

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():    
    assert square(-3) == 9
    assert square(-2) == 4
def test_zero():
    assert square(0) == 0
    


def test_str():
    with pytest.raises(TypeError):
        square("cat")