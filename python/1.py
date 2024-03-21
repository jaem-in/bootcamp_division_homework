"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    a=input()
    a=int(a)
    x=a//100
    y=(a-x*100)//10
    z=a%10

    print(z*100+y*10+x)
    return


if __name__ == '__main__':
    main()
