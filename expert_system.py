from experta import DefFacts, Fact, KnowledgeEngine, Rule, AND, OR, NOT

import data

class CvDExpert(KnowledgeEngine):
    @DefFacts()
    def first_action(self):
        yield Fact(start = 'yes')
    
    @Rule(Fact(start = 'yes'))
    def start(self):
        print('Insert 1 to see if you have normal values, 2 to see if you have symptoms of a cardiovascular disease.', end = '')
        while True:
            choice = input()
            if choice.isdecimal():
                choice = int(choice)
                if choice == 1 or choice == 2:
                    break
                else:
                    print('The number inserted is wrong.', end = '')
            else:
                print('The value inserted is not an integer.', end = '')
        
        if choice == 1:
            print('\nStarting the verification of your values.')
            self.declare(Fact(start_verification = 'yes'))
        else:
            print('\nStarting the diagnosis.')
            self.declare(Fact(start_diagnosis = 'yes'))
    
    def _insert_answer(self, question: str, answers: list = ['yes', 'no'], fact: Fact = None):
        print(question, end = '')
        
        while True:
            answer = input()
            if answer.lower() in answers:
                break
            else:
                print('The input inserted is wrong. Insert [', end = '')
                for i in range(0, len(answers)):
                    print(answers[i], end = '')
                    if i != len(answers) - 1:
                        print('/', end = '')
                    else:
                        print(']', end = '')
        
        if fact != None:
            if answer.lower() == answers[0]:
                self.declare(fact)
    
    def _insert_ranged_answer(self, question: str, ranged_list: list, averages: dict = None, fact: Fact = None):
        print(question, end = '')
        
        while True:
            answer = input()
            if answer.isdecimal():
                answer = int(answer)
                if answer >= ranged_list[0] and answer <= ranged_list[1]:
                    break
                else:
                    print('The input inserted is not a value between ' + str(ranged_list[0]) + ' and ' + str(ranged_list[1]) + '.', end = '')
            else:
                print('The input inserted is wrong.', end = '')
        
        if fact != None:
            if 'systolic' in averages:
                if answer > averages['systolic'] + 15 or answer < averages['systolic'] - 25:
                    self.declare(fact)
            elif 'diastolic' in averages:
                if answer > averages['diastolic'] or answer < averages['diastolic'] - 30:
                    self.declare(fact)
    
    def _insert_height_weight(self, mean: float):
        print('How tall are you (between 30 - 300 centimeters)?', end = '')
        
        while True:
            height = input()
            if height.isdecimal():
                height = int(height)
                if height >= 30 and height <= 300:
                    break
                else:
                    print('The input inserted is not a value between 30 and 300.', end = '')
            else:
                print('The input inserted is wrong.', end = '')
        
        print('How much do you weight (between 30 - 400 kilograms)?', end = '')
        
        while True:
            weight = input()
            if weight.isdecimal():
                weight = float(weight)
                if weight >= 30 and weight <= 400:
                    break
                else:
                    print('The input inserted is not a value between 30 and 400.', end = '')
            else:
                print('The input inserted is wrong.', end = '')
        
        height /= 100
        BMI = weight / (height * height)
        
        if BMI > mean + 5 or BMI < mean - 10:
            self.declare(Fact(abnormal_BMI = 'yes'))
    
    @Rule(Fact(start_verification = 'yes'))
    def start_verification(self):
        averages = data.CvDData().get_cardio_averages()
        self._insert_ranged_answer('How old are you (between 14 - 100, years)?', [14, 100])
        self._insert_answer('What is your gender (M, F)?', ['m', 'f'])
        self._insert_height_weight(averages['BMI'])
        self._insert_ranged_answer('What is your systolic blood pressure (between 80 - 200 mm Hg)?', [80, 200], {'systolic': averages['systolic']}, Fact(abnormal_systolic_pressure = 'yes'))
        self._insert_ranged_answer('What is your diastolic blood pressure (between 50 - 120 mm Hg)?', [50, 120], {'diastolic': averages['diastolic']}, Fact(abnormal_diastolic_pressure = 'yes'))
        self._insert_answer('What is your level of cholesterol (1- well above normal, 2- above normal, 3- normal)?', ['1', '2', '3'], Fact(abnormal_cholesterol = 'yes'))
        self._insert_answer('What is your level of glucose (1- well above normal, 2- above normal, 3- normal)?', ['1', '2', '3'], Fact(abnormal_glucose = 'yes'))
        self._insert_answer('Do you smoke often? [yes/no]', fact = Fact(smoke = 'yes'))
        self._insert_answer('Do you drink alcohol often? [yes/no]', fact = Fact(drink_alcohol = 'yes'))
        self._insert_answer('Do you do physical activity often? [yes/no]', fact = Fact(physical_activity = 'yes'))
        print()
    
    @Rule(AND(OR(Fact(abnormal_BMI = 'yes'), Fact(abnormal_systolic_pressure = 'yes'), Fact(abnormal_diastolic_pressure = 'yes'), Fact(abnormal_cholesterol = 'yes'), Fact(abnormal_glucose = 'yes'), OR(Fact(smoke = 'yes'), Fact(drink_alcohol = 'yes'), NOT(Fact(physical_activity = 'yes')))), NOT(Fact(start_diagnosis = 'yes'))))
    def high_chance_disease(self):
        self.declare(Fact(high_chance_disease = 'yes'))
    
    @Rule(Fact(high_chance_disease = 'yes'))
    def high_chance_disease_print(self):
        print('There is a high chance that you have a heart disease! Please do the diagnosis now.')
    
    @Rule(AND(NOT(Fact(start_diagnosis = 'yes')), NOT(Fact(high_chance_disease = 'yes'))))
    def low_chance_disease(self):
        self.declare(Fact(low_chance_disease = 'yes'))
    
    @Rule(Fact(low_chance_disease = 'yes'))
    def low_chance_disease_print(self):
        print('There is a low chance that you have a heart disease.')
    
    @Rule(Fact(start_diagnosis = 'yes'))
    def start_diagnosis(self):
        self._insert_answer('Do you have chest pain? [yes/no]', fact = Fact(chest_pain = 'yes'))
        self._insert_answer('Do you have chest discomfort (fluttering in the chest)? [yes/no]', fact = Fact(chest_discomfort = 'yes'))
        self._insert_answer('Do you have chest tightness or pressure? [yes/no]', fact = Fact(chest_pressure = 'yes'))
        self._insert_answer('Do you get short of breath during activity or at rest (especially during the night when trying to sleep or when you wake up)? [yes/no]', fact = Fact(shortness_of_breath = 'yes'))
        self._insert_answer('Do you have pain in the neck, jaw, throat, upper belly area or back? [yes/no]', fact = Fact(general_pain = 'yes'))
        self._insert_answer('Do you have pain, numbness, weakness or coldness in the legs or arms? [yes/no]', fact = Fact(limbs_pain = 'yes'))
        self._insert_answer('Do you have syncope or have you been near fainting? [yes/no]', fact = Fact(syncope = 'yes'))
        self._insert_answer('Are you dizzy? [yes/no]', fact = Fact(dizziness = 'yes'))
        self._insert_answer('Do you have lightheadedness? [yes/no]', fact = Fact(lightheadedness = 'yes'))
        self._insert_answer('Do you have tachycardia? [yes/no]', fact = Fact(tachycardia = 'yes'))
        self._insert_answer('Do you have bradycardia? [yes/no]', fact = Fact(bradycardia = 'yes'))
        self._insert_answer('Do you have cyanosis? [yes/no]', fact = Fact(cyanosis = 'yes'))
        self._insert_answer('Have you been swelling in the legs? [yes/no]', fact = Fact(swollen_legs = 'yes'))
        self._insert_answer('Have you been swelling in the belly area? [yes/no]', fact = Fact(swollen_belly = 'yes'))
        self._insert_answer('Do you have swollen hands, ankles or feet? [yes/no]', fact = Fact(swollen_limbs = 'yes'))
        self._insert_answer('Do you get tired during exercise or activity? [yes/no]', fact = Fact(tiredness = 'yes'))
        self._insert_answer('Do you easily feel fatigue? [yes/no]', fact = Fact(fatigue = 'yes'))
        self._insert_answer('Do you have dry, persistent cough or fever? [yes/no]', fact = Fact(fever = 'yes'))
        self._insert_answer('Does your skin rashes? [yes/no]', fact = Fact(skin_rash = 'yes'))
        print()
    
    @Rule(AND(OR(Fact(chest_pain = 'yes'), Fact(chest_discomfort = 'yes'), Fact(chest_pressure = 'yes')), Fact(shortness_of_breath = 'yes'), Fact(general_pain = 'yes'), Fact(limbs_pain = 'yes')))
    def blood_vessels_disease_symptoms(self):
        self.declare(Fact(blood_vessels_disease = 'yes'))
    
    @Rule(Fact(blood_vessels_disease = 'yes'))
    def blood_vessels_print(self):
        print('You have all the symptoms of heart disease in the blood vessels! Go see a doctor.')
    
    @Rule(AND(OR(Fact(chest_pain = 'yes'), Fact(chest_discomfort = 'yes')), Fact(shortness_of_breath = 'yes'), Fact(syncope = 'yes'), OR(Fact(dizziness = 'yes'), Fact(lightheadedness = 'yes')), OR(Fact(tachycardia = 'yes'), Fact(bradycardia = 'yes'))))
    def heart_arrhythmias_symptoms(self):
        self.declare(Fact(heart_arrhythmias = 'yes'))
    
    @Rule(Fact(heart_arrhythmias = 'yes'))
    def heart_arrhythmias_print(self):
        print('You have all the symptoms of heart arrhythmias! Go see a doctor.')
    
    @Rule(AND(Fact(shortness_of_breath = 'yes'), Fact(cyanosis = 'yes'), OR(Fact(swollen_legs = 'yes'), Fact(swollen_belly = 'yes')), Fact(swollen_limbs = 'yes'), Fact(tiredness = 'yes')))
    def congenital_heart_defects_symptoms(self):
        self.declare(Fact(congenital_heart_defects = 'yes'))
    
    @Rule(Fact(congenital_heart_defects = 'yes'))
    def congenital_heart_defects_print(self):
        print('You have all the symptoms of congenital heart defects! Go see a doctor.')
    
    @Rule(AND(Fact(shortness_of_breath = 'yes'), OR(Fact(syncope = 'yes'), Fact(dizziness = 'yes'), Fact(lightheadedness = 'yes')), OR(Fact(tachycardia = 'yes'), Fact(bradycardia = 'yes')), OR(Fact(swollen_legs = 'yes'), Fact(swollen_limbs = 'yes')), Fact(fatigue = 'yes')))
    def cardiomyopathy_symptoms(self):
        self.declare(Fact(cardiomyopathy = 'yes'))
    
    @Rule(Fact(cardiomyopathy = 'yes'))
    def cardiomyopathy_print(self):
        print('You have all the symptoms of cardiomyopathy! Go see a doctor.')
    
    @Rule(AND(Fact(chest_pain = 'yes'), Fact(shortness_of_breath = 'yes'), Fact(syncope = 'yes'), OR(Fact(tachycardia = 'yes'), Fact(bradycardia = 'yes')), OR(Fact(swollen_legs = 'yes'), Fact(swollen_belly = 'yes')), Fact(swollen_limbs = 'yes'), Fact(fatigue = 'yes'), Fact(fever = 'yes'), Fact(skin_rash = 'yes')))
    def valvular_heart_disease_symptoms(self):
        self.declare(Fact(valvular_heart_disease = 'yes'))
    
    @Rule(Fact(valvular_heart_disease = 'yes'))
    def valvular_heart_disease_print(self):
        print('You have all the symptoms of valvular heart disease! Go see a doctor.')
    
    @Rule(AND(NOT(Fact(blood_vessels_disease = 'yes')), NOT(Fact(heart_arrhythmias = 'yes')), NOT(Fact(congenital_heart_defects = 'yes')), NOT(Fact(cardiomyopathy = 'yes')), NOT(Fact(valvular_heart_disease = 'yes')), NOT(Fact(start_verification = 'yes'))))
    def absence_of_symptoms(self):
        self.declare(Fact(absence_of_symptoms = 'yes'))
    
    @Rule(Fact(absence_of_symptoms = 'yes'))
    def absence_of_symptoms_print(self):
        print('You have no symptoms of a cardiovascular disease!')