print("Hello, World!")
tinggi = int(input("Masukkan tinggi: "))

print("\nsegitiga siku-siku")
for i in range(1, tinggi + 1):
    print('*' * i)

print("\nsegitiga terbalik")
for i in reversed(range(1, tinggi + 1)):
    print('*' * i)

print("\nsegitiga siku-siku rata kanan")
for i in reversed(range(1, tinggi + 1)):
    print(' ' * i + '*' * (tinggi - i + 1))

print("\nsegitiga siku-siku terbalik rata kanan")
for i in range(1, tinggi + 1):
    print(' ' * i + '*' * (tinggi - i + 1))

print("\nsegitiga sama kaki")
for i in reversed(range(1, tinggi + 1)):
    print(' ' * i + '*' * (2 * (tinggi - i + 1) - 1))

print("\nsegitiga sama kaki terbalik")
for i in range(1, tinggi + 1):
    print(' ' * i + '*' * (2 * (tinggi - i + 1) - 1))

print("\nwajik")
for i in range(-tinggi, tinggi + 1):
    print(' ' * abs(i) + '*' * (2 * (tinggi - abs(i) + 1) - 1))

print("\njam pasir")
for i in range(-tinggi, tinggi + 1):
    print(' ' * (tinggi - abs(i)) + '*' * (2 * (abs(i) + 1) - 1))