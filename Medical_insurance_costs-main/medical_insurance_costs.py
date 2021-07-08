import csv

#listar las columnas
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

#Función para cargar la data del csv
def data_list(lst, csv_file, column_name):
    #Abrir archivo csv
    with open(csv_file) as csv_data:
        #leer la data
        csv_read = csv.DictReader(csv_data)
        #agrego info de cada columna a la lista
        for row in csv_read:
            lst.append(row[column_name])
        return lst

data_list(ages, 'insurance.csv', 'age')
data_list(sexes, 'insurance.csv', 'sex')
data_list(bmis, 'insurance.csv', 'bmi')
data_list(num_children, 'insurance.csv', 'children')
data_list(smoker_statuses, 'insurance.csv', 'smoker')
data_list(regions, 'insurance.csv', 'region')
data_list(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    #Metodo que toma las listas
    def __init__(self, patients_ages, patients_sexes, patients_bmi, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmi
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges
        #Llamar a los returns
        num_females,num_males = self.analyze_sexes()
        avg_smokers,avg_no_smokers = self.charges_smoker_statuses()
        avg_children_female,avg_children_male = self.charges_family()
        #Printear la info
        print(f"Promedio de edades de pacientes: {self.average_ages()} años")
        print(f"Cantidad de mujeres: {num_females} Cantidad de hombres: {num_males}")
        print(f"Promedio de cargo a fumadores: {avg_smokers}, Promedio de cargo a no fumadores: {avg_no_smokers}")
        print(f"Promedio de gasto con hijos de mujeres: {avg_children_female}, Promedio de gasto con hijos de hombres: {avg_children_male}")

    #Promedio de edades
    def average_ages(self):
        #Inicio las edades en 0
        total_ages = 0
        #Iterate por las edades
        for age in self.patients_ages:
            #Sumar las edades al total
            total_ages += int(age)
        #Calcular el promedio
        average_final = round(total_ages/len(self.patients_ages),2)
        return average_final

    #Metodo para calcular el número de hombres y mujeres
    def analyze_sexes(self):
        #Empezar con ambos en 0
        males = 0
        females = 0
        #Iterate por los sexos
        for sex in self.patients_sexes:
            #Sumatoria de mujeres
            if sex == "female":
                females += 1
            #Sumatoria de hombres
            else:
                males += 1
        return females, males

    #Metodo para diferenciar el promedio de precios entre fumadores y no fumadores
    def charges_smoker_statuses(self):
        smoker_charges = 0
        no_smoker_charges = 0
        #Contar cantidad de fumadores y no fumadores
        num_smokers = 0
        num_no_smokers = 0

        #Iterate por los statuses
        for i in range(len(self.patients_smoker_statuses)):
            status = self.patients_smoker_statuses[i]
            #Smoker statuses
            if status == "yes":
                smoker_charges += float(self.patients_charges[i])
                num_smokers += 1
            #No smoker statuses
            elif status == "no":
                no_smoker_charges += float(self.patients_charges[i])
                num_no_smokers += 1
        #Promedios
        avg_smokers = round(smoker_charges/num_smokers, 2)
        avg_no_smokers = round(no_smoker_charges/num_no_smokers, 2)
        return avg_smokers, avg_no_smokers


        #Promedios
        avg_smokers = round(smoker_charges/num_smokers, 2)
        avg_no_smokers = round(no_smoker_charges/num_no_smokers, 2)
        #Retornar amobos Promedios
        return avg_smokers, avg_no_smokers

    #Metodo para ver el promedio de cargo por familia entre hombres y mujeres
    def charges_family(self):
        #Contar cantidad de hijos
        kids_for_female = 0
        kids_for_male = 0
        #Cargo por hijos
        charges_kids_female = 0
        charges_kids_male = 0

        #Iterate por los números de hijxs
        for i in range(len(self.patients_num_children)):
            gender = self.patients_sexes[i]
            children = int(self.patients_num_children[i])

            #Calcular cantidad de hijxs de mujeres
            if gender == "female" and children > 0:
                kids_for_female += children
                charges_kids_female += float(self.patients_charges[i])


            #Calcular cantidad de hijxs de hombres
            elif gender == "male" and children > 0:
                kids_for_male += children
                charges_kids_male += float(self.patients_charges[i])

            #No hacer nada en caso de que de 0 la catidad de hijxs
            else:
                pass
         #Calcular promedios
        avg_children_female = round(charges_kids_female/kids_for_female, 2)
        avg_children_male = round(charges_kids_male/kids_for_male, 2)


        return avg_children_female, avg_children_male

    #Metodo para ver las distintas regiones
    def unique_regions(self):
        region_names= []

        #Corroborar que la region no esté en la lista, si es así lo agrega
        for region in self.patients_regions:
            if region not in region_names:
                region_names.append(region)

        #Si ya está en la lista, lo agrega
        else:
            pass

        return region_names

    #Metodo par guardar la información en un diccionario
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary

patients_info = PatientsInfo(ages, sexes, bmis,num_children, smoker_statuses, regions, insurance_charges)
