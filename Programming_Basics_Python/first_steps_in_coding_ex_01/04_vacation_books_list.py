total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours = total_pages // pages_per_hour

hours_per_day = total_hours // days

print(hours_per_day)