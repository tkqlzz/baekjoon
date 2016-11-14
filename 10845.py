queue = []
for i in range(int(input())):
    cmd = input()
    if 'push' in cmd:
        cmd, data = cmd.split()
        queue.append(data)
    elif 'pop' in cmd:
        print(queue.pop(0) if queue else '-1')
    elif 'front' in cmd:
        print(queue[0] if queue else '-1')
    elif 'back' in cmd:
        print(queue[-1] if queue else '-1')
    elif 'empty' in cmd:
        print('0' if queue else '1')
    elif 'size' in cmd:
        print(len(queue))