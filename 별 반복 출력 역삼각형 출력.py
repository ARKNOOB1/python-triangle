# 출력 조건: 함수 사용


#출력해야 할 것
#******
# *****
#  ****
#   ***
#    **
#     *


#작동부

def STAR():
    for star in  range(1,10):          # star 안에 1이상 10미만의 수를넣는다. = (1~9)
        for space in range(1,10):      # space 안에 1이상 10 미만의 수를 넣는다. = (1~9)
            if star<space:             # 만약 star가 space보다 작으면 *을 출력하고 *출력마다 *뒤에 "공백"을 출력하고 끝낸다.
                print("*", end=" ")    
            else:                      # 만약 star가 space보다 작지 않으면 "공백"을 출력하고 "공백"출력마다 "공백"뒤에 "공백"을 출력하고 끝낸다. 
                print(" ", end=" ")    
            
        print('')                      # 글자가 밑으로 내려갈때 "공백"을 출력

print(STAR())


#함수 작동 방식

# 1. 함수를 호출하면 star에는 1이 대입된다. 그리고나서 다시 space에도 1이 대입된다.
# 2. if 문에서 star가 space보다 작다는것이 "참"인지 "거짓"인지 확인한다.
# 3-1. 만약 star<space가 "참"이면 *을 출력하고 출력마다 *뒤에 "공백"을 출력한다. (ex: star = 1, space = 2  or  star = 2 space = 3 등등)
# 3-2. 만약 star<space가 "거짓"이면 "공백"을 출력하고 "공백"뒤에 "공백을 출력한다." (ex: star = 1, space = 1  or  star = 2, space = 2 등등)
# 4. space의 수가 1씩늘어난다. -> 3-1와 3-2 반복
# 5. star가 10 미만(9)이 되면 더이상 값을 출력하지 않고 함수를 끝낸다.




