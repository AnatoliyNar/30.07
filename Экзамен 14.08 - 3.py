class Tomato:

    states = {0: 'У вас нет помидора', 1: 'Расток', 2: 'У вас зелёный помидор', 3: 'У вас красно-зеленый помидор', 4: 'У вас прекрасный красный помидор' , 5: 'У вас перегнивщий помидор' }

    
    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()
        
    def is_ripe(self):
        if self._state == 3 or 4:
            return True
        elif self._state == 5:
            return 'Ваш помидор сгнил'
    
class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
  
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print('Садовник хорошо потрудился.')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Ваши плоды созрели.')
        else:
            print('Ваши плоды ещё не созрели.')

    
    
    def knowledge_base():
        print('''Справка, подтверждающая, что реализуемая продукция выращена (произведена) на земельном участке,\n находящемся на территории Республики Беларусь''')


def main():
    
    Gardener.knowledge_base()
    tomato_bush = TomatoBush(4)
    gardener = Gardener(tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

main()
