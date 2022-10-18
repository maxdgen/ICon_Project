import owlready2 as owl

class CvDOntology:
    def __init__(self):
        self.ontology = owl.get_ontology('http://www.semanticweb.org/cardiovascular_disease_symptoms/description_symptoms')
        
        with self.ontology:
            class cardiovascular_disease_symptom(owl.Thing):
                pass
            
            class description_symptom(owl.DataProperty):
                domain = [cardiovascular_disease_symptom]
                
                range = [str]
            
            class chest_pain(cardiovascular_disease_symptom):
                pass
            
            class chest_discomfort(cardiovascular_disease_symptom):
                pass
            
            class chest_pressure(cardiovascular_disease_symptom):
                pass
            
            class shortness_of_breath(cardiovascular_disease_symptom):
                pass
            
            class general_pain(cardiovascular_disease_symptom):
                pass
            
            class limbs_pain(cardiovascular_disease_symptom):
                pass
            
            class syncope(cardiovascular_disease_symptom):
                pass
            
            class dizziness(cardiovascular_disease_symptom):
                pass
            
            class lightheadedness(cardiovascular_disease_symptom):
                pass
            
            class tachycardia(cardiovascular_disease_symptom):
                pass
            
            class bradycardia(cardiovascular_disease_symptom):
                pass
            
            class cyanosis(cardiovascular_disease_symptom):
                pass
            
            class swollen_legs(cardiovascular_disease_symptom):
                pass
            
            class swollen_belly(cardiovascular_disease_symptom):
                pass
            
            class swollen_limbs(cardiovascular_disease_symptom):
                pass
            
            class tiredness(cardiovascular_disease_symptom):
                pass
            
            class fatigue(cardiovascular_disease_symptom):
                pass
            
            class fever(cardiovascular_disease_symptom):
                pass
            
            class skin_rash(cardiovascular_disease_symptom):
                pass
            
        instance_chest_pain = chest_pain(name = 'instance_chest_pain')
        instance_chest_pain.description_symptom = ['Chest pain is a pain in any area of your chest. It can be ' + 
                                                   'sharp or dull and you may feel tightness, achiness, or you may ' + 
                                                   'feel like your chest is being crushed or squeezed. Chest pain ' + 
                                                   'can last for a few minutes or hours.']
        instance_chest_discomfort = chest_discomfort(name = 'instance_chest_discomfort')
        instance_chest_discomfort.description_symptom = ['Anxiety or stress is the root of most chest butterflies — also ' + 
                                                         'referred to as heart palpitations — and they can stimulate a surge ' + 
                                                         'of adrenaline in the body. The adrenaline rush then produces a ' + 
                                                         'faster and stronger than normal heartbeat. That is when you get the ' + 
                                                         'feeling of a butterfly or flutter in the chest.']
        instance_chest_pressure = chest_pressure(name = 'instance_chest_pressure')
        instance_chest_pressure.description_symptom = ['Chest pressure is the sensation of a squeezing, tightening, crushing ' + 
                                                       'or pressing in the chest area, with or without pain. It is sometimes ' + 
                                                       'described as a feeling of a band tightening around your chest or of ' + 
                                                       'something heavy sitting on your chest.']
        instance_shortness_of_breath = shortness_of_breath(name = 'instance_shortness_of_breath')
        instance_shortness_of_breath.description_symptom = ['Shortness of breath — known medically as dyspnea — is often ' + 
                                                            'described as an intense tightening in the chest, air hunger, ' + 
                                                            'difficulty breathing, breathlessness or a feeling of suffocation. ' + 
                                                            'Very strenuous exercise, extreme temperatures, obesity and higher ' + 
                                                            'altitude all can cause shortness of breath in a healthy person.']
        instance_general_pain = general_pain(name = 'instance_general_pain')
        instance_general_pain.description_symptom = ['Neck pain may feel like sharp or stabbing pain that is localized to one area. ' + 
                                                     'Pain when moving. Jaw pain is pain from the muscles that control jaw movement.' + 
                                                     'Throat pain is a pain or a scratchy sensation in the throat. Pain that worsens with ' + 
                                                     'swallowing or talking. Back pain can range from a muscle aching to a shooting, burning ' + 
                                                     'or stabbing sensation. Upper abdomen pain is usually harmless and is the result of either ' + 
                                                     'a muscle strain or something you have eaten.']
        instance_limbs_pain = limbs_pain(name = 'instance_limbs_pain')
        instance_limbs_pain.description_symptom = ['Numbness of legs or arms is a symptom in which a person loses feeling in that ' + 
                                                   'particular part of their body. Muscle weakness happens when your full effort ' + 
                                                   'doesn’t produce a normal muscle contraction or movement. Coldness in your limbs ' + 
                                                   'are related to poor blood circulation or nerve damage in your hands or feet']
        instance_syncope = syncope(name = 'instance_syncope')
        instance_syncope.description_symptom = ['Syncope is the medical term for fainting or passing out. It is caused by a ' + 
                                                'temporary drop in the amount of blood that flows to the brain. Syncope can happen ' + 
                                                'if you have a sudden drop in blood pressure, a drop in heart rate, or changes in the ' + 
                                                'amount of blood in areas of your body. If you pass out, you will likely become conscious ' + 
                                                'and alert right away, but you may be feel confused for a bit.']
        instance_dizziness = dizziness(name = 'instance_dizziness')
        instance_dizziness.description_symptom = ['Dizziness is a term used to describe a range of sensations, such ' + 
                                                  'as feeling faint, woozy, weak or unsteady. Dizziness that creates the ' + 
                                                  'false sense that you or your surroundings are spinning or moving is called vertigo.']
        instance_lightheadedness = lightheadedness(name = 'instance_lightheadedness')
        instance_lightheadedness.description_symptom = ['Lightheadedness is when you feel like you might faint. Your body could feel heavy, ' + 
                                                        'you might feel nauseous and unsteady, and you may sweat. Your vision might also be affected. ' + 
                                                        'Lightheadedness is often caused by a lack of blood in the brain.']
        instance_tachycardia = tachycardia(name = 'instance_tachycardia')
        instance_tachycardia.description_symptom = ['Tachycardia refers to a heart rate that is too fast. How that is ' + 
                                                    'defined may depend on your age and physical condition. Generally speaking, ' + 
                                                    'for adults, a heart rate of more than 100 beats per minute (BPM) is considered too fast.']
        instance_bradycardia = bradycardia(name = 'instance_bradycardia')
        instance_bradycardia.description_symptom = ['Bradycardia is a slow or irregular heart rhythm, usually fewer than 60 beats per minute. ' + 
                                                    'At this rate, the heart is not able to pump enough oxygen-rich blood to your body during ' + 
                                                    'normal activity or exercise. As a result, you may feel dizzy or have chronic lack of energy, ' + 
                                                    'shortness of breath, or even fainting spells.']
        instance_cyanosis = cyanosis(name = 'instance_cyanosis')
        instance_cyanosis.description_symptom = ['Cyanosis is a bluish discoloration of the skin, mucous membranes, ' + 
                                                 'tongue, lips, or nail beds and is due to an increased concentration of ' + 
                                                 'reduced hemoglobin (Hb) in the circulation. Clinically evident cyanosis typically ' + 
                                                 'occurs at an oxygen saturation of 85% or less.']
        instance_swollen_legs = swollen_legs(name = 'instance_swollen_legs')
        instance_swollen_legs.description_symptom = ['Swelling (oedema) of the lower legs and feet happens when fluid in the lower legs ' + 
                                                     'has difficulty returning back up to the heart. Swelling in the lower legs is often caused ' + 
                                                     'by problems with the veins in the lower legs.']
        instance_swollen_belly = swollen_belly(name = 'instance_swollen_belly')
        instance_swollen_belly.description_symptom = ['A swollen abdomen occurs when your stomach area is larger than normal. ' + 
                                                      'This is sometimes known as a distended abdomen or swollen belly. A swollen abdomen ' + 
                                                      'is often uncomfortable or even painful']
        instance_swollen_limbs = swollen_limbs(name = 'instance_swollen_limbs')
        instance_swollen_limbs.description_symptom = ['Hand swelling is typically caused by fluid retention, arthritis, or a rise in your ' + 
                                                      'body temperature. Swelling in the ankles, feet and is often caused by a build-up of ' + 
                                                      'fluid in these areas, called oedema. Oedema is usually caused by: standing or sitting ' + 
                                                      'in the same position for too long. eating too much salty food.']
        instance_tiredness = tiredness(name = 'instance_tiredness')
        instance_tiredness.description_symptom = ['Tiredness is an expected feeling after certain activities or at the ' + 
                                                  'end of the day. Usually, you know why you’re tired, and a good sleep at ' + 
                                                  'night solves the problem.']
        instance_fatigue = fatigue(name = 'instance_fatigue')
        instance_fatigue.description_symptom = ['Fatigue is a daily lack of energy; unusual or excessive whole-body tiredness not relieved ' + 
                                                'by sleep. It can be acute (lasting a month or less) or chronic (lasting from 1 to 6 months or longer). ' + 
                                                'Fatigue can prevent a person from functioning normally and affects the life quality of a person.']
        instance_fever = fever(name = 'instance_fever')
        instance_fever.description_symptom = ['A fever is a body temperature that is higher than normal. A normal temperature ' + 
                                              'can vary from person to person, but it is usually around 98.6 °F (37 °C). A fever ' + 
                                              'is not a disease. It is usually a sign that your body is trying to fight an illness or ' + 
                                              'infection. Infections cause most fevers.']
        instance_skin_rash = skin_rash(name = 'instance_skin_rash')
        instance_skin_rash.description_symptom = ['A rash is an area of irritated or swollen skin. Many rashes are itchy, red, painful, ' + 
                                                  'and irritated. Some rashes can also lead to blisters or patches of raw skin. Rashes are ' + 
                                                  'a symptom of many different medical problems. Other causes include irritating substances and allergies.']
        
    def show_description(self):
        while True:
            print('Insert one of the following numbers to see the description of the chosen symptom, 0 to end:')
            print('1- Chest pain\n2- Chest discomfort\n3- Chest pressure\n4- Shortness of breath\n5- General pain\n6- Limbs pain\n7- Syncope\n8- Dizziness')
            print('9- Lightheadedness\n10- Tachycardia\n11- Bradycardia\n12- Cyanosis\n13- Swollen legs\n14- Swollen belly\n15- Swollen limbs\n16- Tiredness')
            print('17- Fatigue\n18- Fever\n19- Skin rash', end = '')
            while True:
                choice = input()
                if choice.isdecimal():
                    choice = int(choice)
                    if choice < 0 or choice > 19:
                        print('The number inserted is wrong.', end = '')
                    else:
                        if choice == 1:
                            print('\n' + self.ontology.instance_chest_pain.description_symptom[0] + '\n')
                        elif choice == 2:
                            print('\n' + self.ontology.instance_chest_discomfort.description_symptom[0] + '\n')
                        elif choice == 3:
                            print('\n' + self.ontology.instance_chest_pressure.description_symptom[0] + '\n')
                        elif choice == 4:
                            print('\n' + self.ontology.instance_shortness_of_breath.description_symptom[0] + '\n')
                        elif choice == 5:
                            print('\n' + self.ontology.instance_general_pain.description_symptom[0] + '\n')
                        elif choice == 6:
                            print('\n' + self.ontology.instance_limbs_pain.description_symptom[0] + '\n')
                        elif choice == 7:
                            print('\n' + self.ontology.instance_syncope.description_symptom[0] + '\n')
                        elif choice == 8:
                            print('\n' + self.ontology.instance_dizziness.description_symptom[0] + '\n')
                        elif choice == 9:
                            print('\n' + self.ontology.instance_lightheadedness.description_symptom[0] + '\n')
                        elif choice == 10:
                            print('\n' + self.ontology.instance_tachycardia.description_symptom[0] + '\n')
                        elif choice == 11:
                            print('\n' + self.ontology.instance_bradycardia.description_symptom[0] + '\n')
                        elif choice == 12:
                            print('\n' + self.ontology.instance_cyanosis.description_symptom[0] + '\n')
                        elif choice == 13:
                            print('\n' + self.ontology.instance_swollen_legs.description_symptom[0] + '\n')
                        elif choice == 14:
                            print('\n' + self.ontology.instance_swollen_belly.description_symptom[0] + '\n')
                        elif choice == 15:
                            print('\n' + self.ontology.instance_swollen_limbs.description_symptom[0] + '\n')
                        elif choice == 16:
                            print('\n' + self.ontology.instance_tiredness.description_symptom[0] + '\n')
                        elif choice == 17:
                            print('\n' + self.ontology.instance_fatigue.description_symptom[0] + '\n')
                        elif choice == 18:
                            print('\n' + self.ontology.instance_fever.description_symptom[0] + '\n')
                        elif choice == 19:
                            print('\n' + self.ontology.instance_skin_rash.description_symptom[0] + '\n')
                        break
                else:
                    print('The value inserted is not an integer.', end = '')
            if choice == 0:
                break