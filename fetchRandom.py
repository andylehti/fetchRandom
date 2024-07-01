import random

def fetchRandA():
    s = ''.join(random.choice('01') for _ in range(64))
    r = random.randint(0, 512)
    return s[r % len(s)]

def fetchRandB():
    s = ''.join(random.choice('0123456789') for _ in range(100))
    r = random.randint(0, 50)
    b = s[r % len(s)] + s[(r * 2) % len(s)]
    return int(b) % 2

def fetchRandC():
    s = ''.join(random.choice('01') for _ in range(65))
    v = 1 if s.count('1') > s.count('0') else 0
    return v
