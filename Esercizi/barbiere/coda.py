from queue import Queue


coda = Queue (5)
for i in range (5):
    coda.put(i)

print (list(coda.queue))
coda.put(10)
print("seconda print")
print(list(coda.queue))