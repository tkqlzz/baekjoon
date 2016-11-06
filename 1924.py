m, d = map(int, input().split())
m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
for i in range(1, m):
    d += m_days[i]
print(d_week[d % 7])