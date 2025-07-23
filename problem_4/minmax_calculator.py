def main():
    try:
        nums=list(map(float,input("숫자를 입력하세요.").split()))
        min_num=nums[0]
        max_num=nums[0]

        for num in nums[1:]:
            if num<min_num:
                min_num=num
            if num>max_num:
                max_num=num
    except ValueError:
        print("Invalid input.")
    print(f"Min:{min_num},Max:{max_num}")
if __name__ == "__main__":
    main()