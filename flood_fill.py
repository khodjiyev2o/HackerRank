import random 

class Safari():
    def __init__(self,animals:list = ['L','T','W','D']):
            self.animals = animals
            self.safari = []

    ## create 2d array
    def create_safari(self)->list[list]:
        for i in range(10):
            sell = []
            for i in range(10):
                random_animal = random.choice(self.animals)
                sell.append(random_animal)
            self.safari.append(sell)
        return self.safari
    
    ##random_cell
    def get_random_cell(self)->list[int]:
        sell = []
        for i in range(2):
            random_num = random.choice(range(0,10))
            sell.append(random_num)
        return sell
    
    ##get the animal by picked 2d_Array
    def get_animal(self,picked_cell:list,safari:list[list])->str:
        animal = safari[picked_cell[0]][picked_cell[1]]
        return animal


    def conquer(self,picked_animal:str,safari:list[list],cell:int=9)->list[list]:
        
        if picked_animal == "D": ##  Terminate recursion, as deer cannot hunt anyone
            print("Deer cannot hunt noone!")
            return safari

        if cell < 0: ##Terminate recursion , if there are no arrays left
            return safari

        for i in range(0,10): ## Loop through the cell that decrements by recursion

            if picked_animal == "L":
                if safari[cell][i] != "L":
                    safari[cell][i] = "-" ## swap the letters

            elif picked_animal == "T":
                if safari[cell][i] != "T" or "L":
                    safari[cell][i] = "-" ## swap the letters

            elif picked_animal == "W" :
                if safari[cell][i] == "D":
                    safari[cell][i] = "-" ## swap the letters

        return self.conquer(picked_animal=picked_animal,safari=safari,cell=cell-1)
         
        

cls = Safari()
picked_cell = cls.get_random_cell()
safari = cls.create_safari()
picked_animal=cls.get_animal(picked_cell=picked_cell,safari=safari)

conquered_safari = cls.conquer(picked_animal=picked_animal,safari=safari)

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in safari]))



print("This is a conquered safari")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in conquered_safari]))
