import expert_system
import web_ontology

if __name__ == '__main__':
    print('Insert 1 to see if you have symptoms of a cardiovascular disease and 2 to see the descriptions of the symptoms', end = '')
    while True:
        choice = input()
        if choice.isdecimal():
            choice = int(choice)
            if choice == 1 or choice == 2:
                print()
                break
            else:
                print('The number inserted is wrong.', end = '')
        else:
            print('The value inserted is not an integer.', end = '')
    if choice == 1:
        cvd_expert = expert_system.CvDExpert()
        cvd_expert.reset()
        cvd_expert.run()
    
    elif choice == 2:
        cvd_ontology = web_ontology.CvDOntology()
        cvd_ontology.show_description()