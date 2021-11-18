#!/usr/bin/env python3
enemy_positions: list[int] = [5, 10, 15, 20]

def print_enemy():
    print(enemy_positions)

print_enemy()

print(len(enemy_positions))
print(enemy_positions[3])

enemy_positions[0] = 6
print_enemy()

print(enemy_positions[0:2])

enemy_positions.append(25)
print_enemy()

enemy_positions.insert(1,9)
print_enemy()

enemy_positions.remove(6)
print_enemy()

del(enemy_positions[2])
print_enemy()

print_enemy()
print_enemy()

high_score = 'Jim', 256
print(high_score)

high_score = ('Holly', 150)
print(high_score)

# high_score[0] = 'Jim'
name = high_score[0]

print(len(high_score))

print('Holly' in high_score)
actions = {'r': 1, 'l': -1}
print(actions)

actions['r'] = 2
actions['u'] = 1

for key, value in actions.items():
    print('Key:{0}, Value:{1}'.format(key, value))

del (actions['u'])
print(actions)

r = actions.pop('r')
print(actions)
print(r)
class Player:
    position: int = 0

    def move(self, by_amount: int = 1):
        self.position += by_amount

    def show(self):
        print(self.position)


player = Player()
player.move()
player.show()
player.move()
player.show()
player.move()
player.show()
player.move(5)
player.show()
class Vector:
    x: int = 0
    y: int = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class GameObject:
    name: str
    pos: Vector

    def __init__(self, name: str, x_pos: int, y_pos: int) -> None:
        self.name = name
        self.pos = Vector(x_pos, y_pos)

    ### This allows the object to be printed
    def __str__(self) -> str:
        return "{}: ({}, {})".format(self.name, self.pos.x, self.pos.y)

    def move(self, amount: Vector):
        # self.pos += amount
        self.pos.x += amount.x
        self.pos.y += amount.y

    def moveX(self, amount: int):
        self.pos.x += amount

    def moveY(self, amount: int):
        self.pos.y += amount


class Enemy(GameObject):
    health: int

    def __init__(self, name: str, x_pos: int, y_pos: int, health: int) -> None:
        super().__init__(name, x_pos, y_pos)
        self.health = health

    def __str__(self) -> str:
        return super().__str__() + ' Health: {}'.format(self.health)

    def take_damage(self, amount: int):
        self.health -= amount


if __name__ == '__main__':
    game_object = GameObject('Game Object', 1, 2)
    enemy = Enemy('Enemy', 5, 10, 100)

    print(game_object)
    print(enemy)

    enemy.take_damage(20)
    print(enemy)
