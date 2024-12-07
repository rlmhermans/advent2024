with open('input') as file:
    lines = [line.rstrip() for line in file]

safe = 0
recheck = []
for l in lines:
    report = list(map(int, l.split()))   
    lst = report[0]
    total_delta = 0
    stable = True

    for i in report[1:]:
        if stable:
            delta = lst - i
            
            if delta < 0 and total_delta > 0 or delta > 0 and total_delta < 0 or not 1 <= abs(delta) <= 3:
                stable = False
                recheck.append(report)

            lst = i
            total_delta += delta

    if stable: 
        safe += 1

for r in recheck:
    for j in range(len(r)):
        current = r.copy()
        current.pop(j)

        lst = current[0]
        total_delta = 0
        stable = True

        for i in current[1:]:
            if stable:
                delta = lst - i
                
                if delta < 0 and total_delta > 0 or delta > 0 and total_delta < 0 or not 1 <= abs(delta) <= 3:
                    stable = False

                lst = i
                total_delta += delta

        if stable: 
            safe += 1
            break

print(safe)