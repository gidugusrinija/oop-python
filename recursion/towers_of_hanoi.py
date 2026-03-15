def tower_of_hanoi(n, s, a, d):
    if n==1:
        print(f"Move 1 disk from {s} to {d}")
        return
    tower_of_hanoi(n-1, s, d, a)
    print(f"Move {n} disks from {s} to {d}")
    tower_of_hanoi(n-1, a, s, d)

tower_of_hanoi(3,"A", "B", "C")
