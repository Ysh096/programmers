# 선행 스킬 순서 skill과 유저들이 만든 스킬트리를 담은 배열 skill_trees가 매개변수로 주어짐
# 가능한 스킬트리 개수를 return 하는 함수 solution을 작성하라.

# 스킬은 알파벳 대문자 표기, 모든 문자열이 대문자로만 이루어져 있다.
# 스킬 순서와 스킬트리는 문자열로 표기, C->B->D = "CBD"
# 스킬은 중복해 주어지지 않는다.

# 1. skill에 들어있는 문자를 순서대로 스택에 쌓으면서, 이 때 바로 앞의 문자가 스택에 이미 존재하는지만 확인하면 되지 않을까?
# 존재하지 않는다면 불가능한 스킬트리!
# 2. 그냥 CBD를 하나하나 찾아서 인덱스를 저장한 후 비교해도 될 듯

def solution(skill, skill_trees):
    '''
    skill: 맞춰야 하는 스킬트리의 순서
    skill_trees: 사용자가 원하는 스킬트리 순서
    return: 스킬트리가 몇 개나 가능한가?
    '''
    minus = 0
    for user in skill_trees:
        stack = []
        for s in user:
            if s in skill:
                stack.append(s)
        while stack:
            last = stack.pop()
            last_idx = skill.find(last)
            if last_idx == 0 and len(stack) != 0: # C가 뽑혀 나왔으면 스택이 비어있어야 함
                minus += 1
                break
            elif last_idx == 0 and len(stack) == 0: # C가 뽑혀 나왔는데 스택이 비어있으면 그대로 종료
                break
            elif last_idx != 0 and len(stack) == 0: # 맨 처음 스킬이 아닌걸 뽑았는데 스택이 비어있으면
                minus += 1
                break
            elif skill[last_idx-1] != stack[-1]: # 이전 스킬이 옳지 않으면
                minus += 1
                break
    return len(skill_trees) - minus


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)