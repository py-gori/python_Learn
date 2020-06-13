count = int(input())
key_word = input()

log_L = []
for i in range(count):
    log = input()
    if key_word in log:
        log_L.append(log)

if not log_L:
    print("None")
else:
    for i in log_L:
        print(i)