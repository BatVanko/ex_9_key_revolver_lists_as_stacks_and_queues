from collections import deque

price_per_bullet = int(input())
size_of_the_gun_barrel = int(input())
size = size_of_the_gun_barrel
bullets_shot = 0
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_the_intelligence = int(input())

while bullets and locks:
    if size == 0:
        print("Reloading!")
        size = size_of_the_gun_barrel
    current_bullet = bullets.pop()
    bullets_shot += 1
    current_lock = locks.popleft()
    size -= 1
    if current_lock < current_bullet:
        locks.appendleft(current_lock)
        print("Ping!")
    else:
        print("Bang!")

if not locks:
    all_bullets_shot_price = bullets_shot * price_per_bullet
    money_earned = value_of_the_intelligence - all_bullets_shot_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")