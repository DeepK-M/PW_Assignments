# Base class
class MenuItem:
    __id_counter = 1   # Class variable for unique ID (encapsulation)

    def __init__(self, name, description, price, category):
        self.__id = MenuItem.__id_counter   # Private ID
        MenuItem.__id_counter += 1
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    # Getter for ID (Encapsulation)
    def get_id(self):
        return self.__id

    # Update menu item details
    def update_item(self, name=None, description=None, price=None, category=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        if category:
            self.category = category

    def display_item(self):
        print(f"[{self.__id}] {self.name} - {self.category}")
        print(f"   {self.description}")
        print(f"   Price: ₹{self.price}\n")


# Subclass: Food Item
class FoodItem(MenuItem):
    def __init__(self, name, description, price, category, is_veg=True):
        super().__init__(name, description, price, category)
        self.is_veg = is_veg

    def display_item(self):
        veg_status = "Veg" if self.is_veg else "Non-Veg"
        print(f"[{self.get_id()}] {self.name} ({veg_status}) - {self.category}")
        print(f"   {self.description}")
        print(f"   Price: ₹{self.price}\n")


# Subclass: Beverage Item
class BeverageItem(MenuItem):
    def __init__(self, name, description, price, category, is_cold=True):
        super().__init__(name, description, price, category)
        self.is_cold = is_cold

    def display_item(self):
        temp_status = "Cold" if self.is_cold else "Hot"
        print(f"[{self.get_id()}] {self.name} ({temp_status}) - {self.category}")
        print(f"   {self.description}")
        print(f"   Price: ₹{self.price}\n")


# Restaurant Management System
class Restaurant:
    def __init__(self):
        self.menu = []

    # Add menu item
    def add_item(self, item):
        self.menu.append(item)
        print(f"✅ Item '{item.name}' added successfully!")

    # Remove menu item by ID
    def remove_item(self, item_id):
        for item in self.menu:
            if item.get_id() == item_id:
                self.menu.remove(item)
                print(f"❌ Item '{item.name}' removed successfully!")
                return
        print("⚠️ Item not found!")

    # Display menu
    def show_menu(self):
        print("\n📋 Restaurant Menu:")
        if not self.menu:
            print("   (No items yet!)")
        else:
            for item in self.menu:
                item.display_item()


# ----------- Testing the System -----------
if __name__ == "__main__":
    restaurant = Restaurant()

    # Create items
    pizza = FoodItem("Pizza", "Cheesy delight with toppings", 250, "Main Course", is_veg=True)
    burger = FoodItem("Burger", "Chicken burger with fries", 180, "Snacks", is_veg=False)
    coke = BeverageItem("Coca Cola", "Refreshing cold drink", 50, "Beverage", is_cold=True)
    tea = BeverageItem("Masala Tea", "Hot Indian spiced tea", 40, "Beverage", is_cold=False)

    # Add items to menu
    restaurant.add_item(pizza)
    restaurant.add_item(burger)
    restaurant.add_item(coke)
    restaurant.add_item(tea)

    # Show full menu
    restaurant.show_menu()

    # Update an item
    burger.update_item(price=200, description="Delicious chicken burger with extra cheese")
    print("\n🔄 After Update:")
    restaurant.show_menu()

    # Remove an item
    restaurant.remove_item(coke.get_id())
    print("\n📋 After Removal:")
    restaurant.show_menu()



# Sample Output:
# ✅ Item 'Pizza' added successfully!
# ✅ Item 'Burger' added successfully!
# ✅ Item 'Coca Cola' added successfully!
# ✅ Item 'Masala Tea' added successfully!

# 📋 Restaurant Menu:
# [1] Pizza (Veg) - Main Course
#    Cheesy delight with toppings
#    Price: ₹250

# [2] Burger (Non-Veg) - Snacks
#    Chicken burger with fries
#    Price: ₹180

# [3] Coca Cola (Cold) - Beverage
#    Refreshing cold drink
#    Price: ₹50

# [4] Masala Tea (Hot) - Beverage
#    Hot Indian spiced tea
#    Price: ₹40


# 🔄 After Update:

# 📋 Restaurant Menu:
# [1] Pizza (Veg) - Main Course
#    Cheesy delight with toppings
#    Price: ₹250

# [2] Burger (Non-Veg) - Snacks
#    Delicious chicken burger with extra cheese
#    Price: ₹200

# [3] Coca Cola (Cold) - Beverage
#    Refreshing cold drink
#    Price: ₹50

# [4] Masala Tea (Hot) - Beverage
#    Hot Indian spiced tea
#    Price: ₹40

# ❌ Item 'Coca Cola' removed successfully!

# 📋 After Removal:

# 📋 Restaurant Menu:
# [1] Pizza (Veg) - Main Course
#    Cheesy delight with toppings
#    Price: ₹250

# [2] Burger (Non-Veg) - Snacks
#    Delicious chicken burger with extra cheese
#    Price: ₹200

# [4] Masala Tea (Hot) - Beverage
#    Hot Indian spiced tea
#    Price: ₹40