"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    year=int(input())
    month=int(input())
    mon30=[4,6,9,11]
    mon31=[1,3,5,7,8,10,12]
    if month in mon30:
        print("30")
    elif month in mon31:
        print("31")
    elif month==2 and year%4==0 and year%100!=0:
        print("29")
    elif month==2 and year%400==0:
        print("29")
    elif month==2:
        print("28")


    return


if __name__ == '__main__':
    main()
