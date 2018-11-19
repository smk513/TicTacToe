import random


# 맵 초기화 함수
def resetMap(map):
    map = []
    for i in range(9):
        map.append(" ")
    return map

# 맵 출력
def printMap_All(map):
    print("┌───┬───┬───┐")
    print(printMap_l1(map))
    print("├───┼───┼───┤")
    print(printMap_l2(map))
    print("├───┼───┼───┤")
    print(printMap_l3(map))
    print('└───┴───┴───┘')
    
def printMap_l1(map): 
    return ("│ " + map[0] + " │ " + map[1] + " │ " + map[2] + " │")
    
def printMap_l2(map): 
    return ("│ " + map[3] + " │ " + map[4] + " │ " + map[5] + " │") 
    
def printMap_l3(map): 
    return ("│ " + map[6] + " │ " + map[7] + " │ " + map[8] + " │")

# 문자 지정
def setChar(char, check):
    if (check == ""):
        while(char==' '):
            char = input("다시 입력 하세요 : ")
    else:
        while(char==' ' or char == check):
            char = input("다시 입력 하세요 : ")
    return char

# 시작 순서 결정
def whoFirst():
    if random.randint(0, 1) == 0:
        return "usr"
    else:
        return "com"
    
# 게임 종료 판단
def checkMap(map): 
    for i in range(9):
        if map[i] == ' ':
            result = 1
            break
        else:
            result = 0
    return result

# 승리 확인
def checkWin(map, char): 
    if (map[0] == map[3] == map[6] == char) or \
        (map[1] == map[4] == map[7] == char) or \
        (map[2] == map[5] == map[8] == char) or \
        (map[0] == map[1] == map[2] == char) or \
        (map[3] == map[4] == map[5] == char) or \
        (map[6] == map[7] == map[8] == char) or \
        (map[0] == map[4] == map[8] == char) or \
        (map[2] == map[4] == map[6] == char):
            return 1
    return 0

# 맵 복사
def copyMap(map):
    tmpMap = []
    for i in map:
        tmpMap.append(i)
    return tmpMap
    
# 컴퓨터 입력
def setComCheck(map, comChar):
    # 1. 컴퓨터가 이길 수 있는 수를 찾아서 둔다. (공격)
    for i in range(9):
        tmpMap = copyMap(map)
        if checkExist(tmpMap, i) == 0:
            tmpMap[i] = comChar
            if checkWin(tmpMap, comChar):
                map[i] = comChar
                return 0

    # 2. 사용자가 이길 수 있는 수를 찾아서 막는다. (방어)
    for i in range(9):
        tmpMap = copyMap(map)
        if checkExist(tmpMap, i) == 0:
            tmpMap[i] = usrChar
            if checkWin(tmpMap, usrChar):
                map[i] = comChar
                return 0
    
    # 3. 가장 수가 많이 나오는 중앙이 비어있으면 중앙에 둔다. (4)
    if checkExist(map, 4) == 0:
        map[4] = comChar
        return 0

    # 4. 다음으로 수가 많이 나오는 모서리에 수를 둔다. (0, 2, 6, 8)
    for i in 0, 2, 6, 8:
        if checkExist(map, i) == 0:
            map[i] = comChar
            return 0
    
    # 5. 테두리에 수를 둔다. (1, 3, 5, 7)
    for i in 1, 3, 5, 7:
        if checkExist(map, i) == 0:
            map[i] = comChar
            return 0
    
# 사용자 입력 예외처리 함수
def checkExist(map, idx):
    if map[idx] != " ":
        return 1
    return 0
    
###################################################################
            

map = resetMap(map)    

usrChar = input("사용자 문자 입력 : ")
usrChar = setChar(usrChar, "")

comChar = input("컴퓨터 문자 입력 : ")
comChar = setChar(comChar, usrChar)
print("\n================\n")

turn = whoFirst()
if turn == "usr":
    print("사용자 부터 시작 !")
    printMap_All(map)
else:
    print("컴퓨터 부터 시작 !")

while(checkMap(map)==1):
    if turn == "usr":
        loc = int(input("위치를 입력하세요 : ")) - 1
        while(checkExist(map, loc)):
            loc = int(input("위치를 다시 입력하세요 : ")) - 1
        
        # 사용자 턴 시작
        map[loc] = usrChar
        if checkWin(map, usrChar) == 1:
            printMap_All(map)
            print("사용자 승리!")
            break
        print("\n======== 컴퓨터 턴 ========\n")
        printMap_All(map)
        turn = "com"
        
    else:
        # 컴퓨터 턴 시작
        setComCheck(map, comChar)
        
        if checkWin(map, comChar) == 1:
            printMap_All(map)
            print("컴퓨터 승리!")
            break
        print("\n======== 사용자 턴 ========\n")
        printMap_All(map)
        turn = "usr"

if checkMap(map)==0:
    print("무승부 !")
else:
    print("게임 종료 !")