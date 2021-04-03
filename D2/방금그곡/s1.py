# 음악의 길이는 #을 고려해야 한다. 3#4#5#의 길이 = 3

def solution(m, musicinfos):
    answer = []
    for musicinfo in musicinfos:
        music = musicinfo.split(',') # 리스트 형태로 변경
        # 시간
        time = (int(music[1][0:2]) - int(music[0][0:2])) * 60 + int(music[1][3:5]) - int(music[0][3:5])
        # 음악 정보는 music[3]에 담겨있음.
        music_restruction = []
        for i in range(len(music[3])):
            if music[3][i] == '#':
                music_restruction[-1] += '#'
            else:
                music_restruction.append(music[3][i])
        # 이제 music_restruction은 ['C', 'C#', 'B', 'C', 'C#', 'B'] 이런 형태! #을 하나로 묶음
        music_length = len(music_restruction)

        # 주어진 시간동안 연주된 멜로디
        melody = music_restruction * (time // music_length)
        for i in range(time % music_length):
            melody.append(music_restruction[i])
        # 이제 melody에는 매 분마다 연주된 음이 들어있게 됨

        # 네오가 기억한 멜로디도 #을 하나로 묶은 리스트로 만들자.
        m_restruction = []
        for i in range(len(m)):
            if m[i] == '#':
                m_restruction[-1] += '#'
            else:
                m_restruction.append(m[i])

        # 네오가 기억한 멜로디의 길이가 전체 멜로디보다 길면 바로 다음 음악 정보로!
        if len(m_restruction) > len(melody):
            continue

        k = 0
        while k < len(melody):
            flag = False # while문을 도중에 종료해야 할 때 사용할 것
            cnt = 0 # 네오의 기억과 곡의 멜로디가 얼마나 일치하는지 저장
            right = False # 기본적으로 False, 같은걸 찾으면 True
            if melody[k] == m_restruction[0]: # 시작 부분이 같으면,
                for j in range(len(m_restruction)):
                    if k + j >= len(melody): # 인덱스가 멜로디보다 길어지면
                        flag = True # while문 종료해야함
                        break
                    if melody[k+j] == m_restruction[j]: # 길지 않으면 비교하고,
                        cnt += 1 # 같으면 한 음 일치함을 표시
                    else:
                        k += 1 # 같지 않으면 멜로디의 다음 음을 확인(더 좋은 알고리즘이 있을텐데 일단 브루트포스)
                        # 원래 k += cnt 를 썼었으나 m=CDCDF / melody=CDCDCDF 인 경우 CDCD를 건너뛰어 CDF부터 찾기 때문에 실패..

                # for 문이 끝나고 몇 가지 검사 실시
                if flag == True:
                    break # 인덱스가 멜로디보다 길어졌으면 while문 나가기
                if cnt == len(m_restruction):
                    right = True
                    break # 일치하면 while문 나가기
            # 시작 부분이 같지 않으면
            else:
                k += 1
        # while문이 끝나고 난 후
        if right:
            answer.append((music[2], time))

    # 조건 일치하는 음악이 여러 개인 경우
    if len(answer) > 1:
        how_long = 0
        idx = 0
        cnt = 0
        for ans in answer:
            if ans[1] > how_long: # 재생된 시간이 같은 애는 맨 앞의 것만 따지게 됨
                how_long = ans[1]
                idx = cnt
            cnt += 1
        return (answer[idx][0])
    elif len(answer) == 1:
        return (answer[0][0]) # 조건 일치하는 음악이 한 개인 경우
    else:
        return "(None)" # 없는 경우

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# return "HELLO"
print(solution(m, musicinfos))

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# return FOO
print(solution(m, musicinfos))

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# return WORLD
print(solution(m, musicinfos))