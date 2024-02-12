from collections import deque


def resolved_challenge(result, tool_list, substance_list, challenge_list):
    tool_list.popleft()
    substance_list.pop()
    challenge_list.remove(result)
    return tool_list, substance_list, challenge_list


def not_resolved_challenge(tool_list, substance_list):
    tool_list[0] += 1
    tool_list.rotate(-1)
    substance_list[-1] -= 1
    if substance_list[-1] <= 0:
        substance_list.pop()
    return tool_list, substance_list


tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

current_result = 0

while tools and substances:
    current_tool = tools[0]
    current_substance = substances[-1]
    current_result = current_tool * current_substance
    if current_result in challenges:
        tools, substances, challenges = resolved_challenge(current_result, tools, substances, challenges)
    else:
        tools, substances = not_resolved_challenge(tools, substances)
    current_result = 0

if len(challenges) > 0:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
