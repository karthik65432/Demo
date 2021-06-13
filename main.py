class Student:
    School = 'Telusko'

    def __init__(self, name, rollno,cpu):
        self.name = name
        self.rollno = rollno
        self.lap = self.config(cpu)

    class config:

        def __init__(self, cpu='i5',ram='8gb'):
            self.cpu = cpu
            self.ram = ram


s1= Student('Karthik',1245978,'i7')
print(s1.lap.cpu)



