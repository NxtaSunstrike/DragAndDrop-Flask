
print(sum([i for i in [int(input()) for _ in range(int(input()))]if str(i)[-1:] == '8']))

print(sum([i for i in [int(input()) for _ in range(int(input()))]if str(i)[-1:] == '9']))


print(min([i for i in [int(input()) for _ in range(int(input()))]if i%3 == 0]))

print(len([i for i in [int(input()) for _ in range(int(input()))]if i%4 == 0 and i %7!=0]))

print(min([i for i in [int(input()) for _ in range(int(input()))]if i%2 == 0]))

class Speed(object):
    def __init__(self,cars: list[int])->None:
        self.cars = cars

    def __str__(self)->str:
        return  f'Разность - {max(self.cars)- min(self.cars)} Количество - {len([i for i in self.cars if i<=30])}'

if __name__ == '__main__':
    print(Speed([int(input()) for _ in range(int(input()))]))