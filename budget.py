class Category:

  def __init__(self,name):
    self.name = name
    self.ledger = []
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": description})
        return True
    return False

  def get_balance(self):
    return sum(entry["amount"] for entry in self.ledger)

  def transfer(self, amount, category):
    if self.check_funds(amount):
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for entry in self.ledger:
        description = entry["description"][:23].ljust(23)
        amount = "{:.2f}".format(entry["amount"]).rjust(7)
        items += f"{description}{amount}\n"
        total += entry["amount"]
    output = title + items + "Total: {:.2f}".format(total)
    return output

def create_spend_chart(categories):
    
  total_withdrawals = sum(category.get_withdrawals() for category in categories)
    
  percentages = [(category.get_withdrawals() / total_withdrawals) * 100 for category in categories]

  chart = "Percentage spent by category\n"
  
  for i in range(100, -10, -10):
    chart += f"{i:3d}| {' '.join('o' if percent >= i else ' ' for percent in percentages)}\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_category_name_length = max(len(category.name) for category in categories)
    
    for i in range(max_category_name_length):
        chart += "     "
        for category in categories:
          if i < len(category.name):
            chart += f"{category.name[i]}  "
    else:
            chart += "   "
    if i != max_category_name_length - 1:
      chart += "\n"

    for i in range(max_category_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i != max_category_name_length - 1:
            chart += "\n"

    return chart