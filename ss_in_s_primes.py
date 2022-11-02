f = open('input.txt', 'r')

len_ss, len_s = map(int, f.readline().split())
ss = f.readline()
s = f.readline()

# get the dictionary with the distinct prime number for every letter.
primes = [2]
i = 2
while len(primes) < 52:
    p = 0
    is_prime = True
    while p < len(primes) and is_prime:
        if i % primes[p] == 0:
            is_prime = False
        p += 1
    if is_prime:
        primes.append(i)
    i += 1

ltrs = [chr(i) for i in list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))]
d = {l:i for l, i in zip(ltrs, primes)}

hsh_ss = 1

for i in range(len_ss):
    hsh_ss *= d[ss[i]]

count = 0

hsh_s = 1

for i in range(len_s):
    hsh_s *= d[s[i]]
    if i >= len_ss:
        hsh_s /= d[s[i - len_ss]]

    if hsh_s == hsh_ss:
        count += 1

print(count)
