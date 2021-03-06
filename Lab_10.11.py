# Andrew Li
# 1824794
class FoodItem:
    def __init__(self, name="None", fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_servings = float(input())

    food_1 = FoodItem()
    total_calories1 = food_1.get_calories(num_servings)
    food_1.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, total_calories1))
    print()
    food2 = FoodItem(name, fat, carbs, protein)
    total_calories2 = food2.get_calories(num_servings)
    food2.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, total_calories2))

