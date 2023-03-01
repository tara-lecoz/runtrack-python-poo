class student:
    def __init__(self, nom, prenom, numero_etudiant, credit):
       self.__nom = nom
       self.__prenom = prenom
       self.numero_etudiant = numero_etudiant
       self.__credit = credit
       self.__level = self.__studentEval()

    def add_credits(self, credit):
        self.__credit += credit
        self.__level = self.__studentEval()

    def get_credit(self):
        return self.__credit

    def get_level(self):
        return self.__level

    def set_credit(self, credit):
        self.__credit = credit
        self.__level = self.__studentEval()

    def set_level(self, level):
        self.__level = level
        self.__studentEval()

    def __str__(self):
        return f'Nom = {self.__nom} \nPrénom = {self.__prenom} \nID = {self.numero_etudiant}\nNombre de crédits = {self.__credit}'

    def __studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Très bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(self)
        print(f'Niveau = {self.__level}')

student1 = student("Tara", "Le Coz", 824)
student1.add_credits(120)
student1.studentInfo()

student2 = student("John", "Doe", 145)
student2.add_credits(70)
student2.studentInfo()