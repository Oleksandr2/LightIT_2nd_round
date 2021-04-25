import random
from random import randint

class Player:
    
    # Инициализация характеристик игрока
    def __init__(self):
        self.hit_points = 100
        self.max_hit_points = 100
        self.damage = 1
        self.heal_hit_points = 1
     
    # Выбор действия для игрока :
    # 0 - урон в небольшом диапазоне от 18 до 25
    # 1 - урон в большом диапазоне от 10 до 35
    # 2 - исцеление в диапазоне от 18 до 25	   
    def damage_and_heal(self):
        choice_of_action = random.randint(0,2)
        if choice_of_action == 0:
            self.damage = random.randint(18, 25)
            print("Игрок нанес урон в небольшом диапазоне {}".format(self.damage))
            print()
            return self.damage
            
        if choice_of_action == 1:
            self.damage = random.randint(10, 35)
            print("Игрок нанес урон в небольшом диапазоне {}".format(self.damage))
            print()
            return self.damage
            
        if choice_of_action == 2:
            self.heal_hit_points = random.randint(18, 25)
            self.hit_points += self.heal_hit_points
           
            # Проверка на то превышают ли очки здоровья максимальное значение
            if self.hit_points > self.max_hit_points:  
                self.hit_points = self.max_hit_points 
            print("Игрок восстановил хп на +{}".format(self.heal_hit_points))
            print()
            
class Computer:
    
    # Инициализация характеристик компьютера
    def __init__(self):
        self.hit_points = 100
        self.max_hit_points = 100
        self.damage = 1
        self.heal_hit_points = 1
     
    # Выбор действия для компьютера если очки здоровья больше 35:
    # 0 - урон в небольшом диапазоне от 18 до 25
    # 1 - урон в большом диапазоне от 10 до 35
    # 2 - исцеление в диапазоне от 18 до 25   
    def damage_and_heal(self):
        if self.hit_points > 35:
            choice_of_action = random.randint(0,2)
            if choice_of_action == 0:
                self.damage = random.randint(18, 25)
                print("Компьютер нанес урон в небольшом диапазоне {}".format(self.damage))
                print()
                return self.damage
                
            if choice_of_action == 1:
                self.damage = random.randint(10, 35)
                print("Компьютер нанес урон в большом диапазоне {}".format(self.damage))
                print()
                return self.damage
                
            if choice_of_action == 2:
                self.heal_hit_points = random.randint(18, 25)
                self.hit_points += self.heal_hit_points
                
                # Проверка на то превышают ли очки здоровья максимальное значение
                if self.hit_points > self.max_hit_points:
                    self.hit_points = self.max_hit_points
                print("Компьютер восстановил хп на +{}".format(self.heal_hit_points))
                print()
        
	    # Выбор действия для компьютера если очки здоровья меньше 35:
        # 0 - урон в небольшом диапазоне от 18 до 25
        # 1 - урон в большом диапазоне от 10 до 35
        # 2,3 - исцеление в диапазоне от 18 до 25         
        else: 
            choice_of_action = random.randint(0,3)
            if choice_of_action == 0:
                self.damage = random.randint(18, 25)
                print("Компьютер нанес урон в небольшом диапазоне {}".format(self.damage))
                print()
                return self.damage
                
            if choice_of_action == 1:
                self.damage = random.randint(10, 35)
                print("Компьютер нанес урон в большом диапазоне {}".format(self.damage))
                print()
                return self.damage
                
            if choice_of_action == 2:
                self.heal_hit_points = random.randint(18, 25)
                self.hit_points += self.heal_hit_points
                
                # Проверка на то превышают ли очки здоровья максимальное значение
                if self.hit_points > self.max_hit_points:
                    self.hit_points = self.max_hit_points
                print("Компьютер восстановил хп на +{}".format(self.heal_hit_points))
                print()
                
            if choice_of_action == 3:
                self.heal_hit_points = random.randint(18, 25)
                self.hit_points += self.heal_hit_points
                
                # Проверка на то превышают ли очки здоровья максимальное значение
                if self.hit_points > self.max_hit_points:
                    self.hit_points = self.max_hit_points
                print("Компьютер восстановил хп на +{}".format(self.heal_hit_points))
                print()

# Класс Fight моделирует игровой процесс
class Fight:
    
    # Инициализация участников
    def __init__(self):
        self.computer = Computer()
        self.player = Player()
    
    # Выбор того, кто ходит:
    # 1 - ход Компьютера
    # 2 - ход Игрока    
    def choice_forward(self):
        return random.randint(1,2)
    
    def start(self):
        # Действие продолжается пока здоровье обоих игроков больше 0 
        while (self.player.hit_points > 0 and self.computer.hit_points > 0):    
        
            print()
            print("Computer: {}/{}".format(self.computer.hit_points, self.computer.max_hit_points))
            print("Player: {}/{}".format(self.player.hit_points, self.player.max_hit_points))
            print()
            choice = self.choice_forward()
            if choice == 1:
                choice_of_action = self.computer.damage_and_heal()
                if choice_of_action == 0 or 1:
                    self.player.hit_points -= self.computer.damage
                    
            if choice == 2:
                choice_of_action = self.player.damage_and_heal()
                if choice_of_action == 0 or 1:
                    self.computer.hit_points -= self.player.damage
        
        # Если очки здоровья одного из игроков меньше либо равно 0 
        # выводится сообщение о проигрыше
        else:
            if self.player.hit_points > 0 and self.computer.hit_points <= 0:
                print("Computer lose")
            
            if self.player.hit_points <= 0 and self.computer.hit_points > 0:
                print("Player lose")

# Главная функция                
def main():
    fight = Fight()
    fight.start()
    
main()