from hello.domains import myRandom, my100


class Quiz10:
    def quiz10bubble(self) -> str:
        arr = []
        for i in range(0, 10):
            ran = my100()
            if ran not in arr:
                arr.append(ran)

        for i in range(0, len(arr)):
            for j in range(0, len(arr)-1):
                if arr[j] > arr[j+1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'버블정렬: {arr}')
        return None

    def quiz11insertion(self) -> str:
        arr = []
        for i in range(0, 10):
            ran = my100()
            if ran not in arr:
                arr.append(ran)

        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
        print(f'삽입정렬: {arr}')
        return None

    def quiz12selection(self) -> str:
        arr = []
        for i in range(0, 10):
            ran = my100()
            if ran not in arr:
                arr.append(ran)

        for i in range(0, len(arr)-1):
            min = i
            j = i + 1
            for j in range(j, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        print(f'선택정렬: {arr}')
        return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str:
        num1 = myRandom(2, 50)
        num2 = myRandom(51, 100)
        prime = []
        count = 0
        for i in range(num1, num2+1):
            flag = 1
            for j in range(2, i):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                prime.append(i)
                count += 1
        print(f'{num1}과 {num2} 사이의 소수는 {prime} 총 {count}개 입니다.')
        return None

    def quiz18golf(self) -> str:
        answer = my100()
        num = my100()
        count = 0
        while 1:
            count += 1
            if num > answer:
                print(num)
                print('정답보다 큽니다. 더 작은 값이 출력됩니다.')
                num = myRandom(1, num)
            elif num < answer:
                print(num)
                print(' 정답보다 작습니다. 더 큰 값이 출력됩니다.')
                num = myRandom(num, 100)
            else:
                print(f'정답:{answer} {count}번째에 맞췄습니다.')
                break

        return None

    def quiz19booking(self) -> str:

        return None