class Boss:
    def __init__(self, name: str, company: str):
        self.name = name
        self.company = company
        self.workers = []


class Worker:
    def __init__(self, name: str, company: str, boss: Boss):
        self.name = name
        self.company = company
        self._boss = boss
        boss.workers.append(self)

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if self.company == new_boss.company:
            self._boss.workers.remove(self)
            new_boss.workers.append(self)
            self._boss = new_boss


boss_1 = Boss('John', 'Microsoft')
boss_2 = Boss('Tim', 'Microsoft')
worker_1 = Worker('Tonny', 'Microsoft', boss_1)

assert worker_1.boss == boss_1
assert boss_1.workers[0].name == 'Tonny'
worker_1.boss = boss_2
assert worker_1.boss == boss_2
