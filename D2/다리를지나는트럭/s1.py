# def solution(bridge_length, weight, truck_weights):
#     bridge = [0]*bridge_length
#     bridge[-1] = truck_weights.pop(0)
#     time = 1
#     while bridge: # 더 넣을 트럭이 없어질 때 까지
#         bridge.pop(0)
#         time += 1
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 new_truck = truck_weights.pop(0) # 한계 하중을 넘지 않으면
#                 bridge.append(new_truck)
#             else: # 한계 하중을 넘으면
#                 bridge.append(0)
#         else:
#             pass
#     return time
#
# t = solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
# print(t)

# 개선
def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    bridge[-1] = truck_weights.pop(0)
    time = 1
    W = bridge[-1]
    while bridge: # 더 넣을 트럭이 없어질 때 까지
        W -= bridge[0]
        bridge.pop(0)
        time += 1
        if truck_weights:
            if W + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0)) # 한계 하중을 넘지 않으면
                W += bridge[-1]
            else: # 한계 하중을 넘으면
                bridge.append(0)
        else:
            pass
    return time

t = solution(2, 10, [7, 4, 5, 6])
print(t)