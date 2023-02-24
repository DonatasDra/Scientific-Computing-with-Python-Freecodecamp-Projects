class Category:
    
    def __init__(self, x):
        self.name = x
        self.ledger = list()

    def deposit(self, amount, desc = ''):
        self.ledger.append({'amount' : amount, 'description' : desc})

    def withdraw(self, amount, desc = ''):
        check = self.check_funds(amount)
        if check == True:
            amount = float('-' + str(amount))
            self.ledger.append({'amount': amount, 'description' : desc})
            return True
        else:
            return False
   
    def get_balance(self):
        balance = 0
        for line in range(len(self.ledger)):
            balance += self.ledger[line]['amount']
        return balance
    
    def transfer(self, amount, cat):
        if self.check_funds(amount) == True:
            self.withdraw(amount, ('Transfer to ' + cat.name))
            cat.deposit(amount, ('Transfer from ' + self.name))
            return True
        else:
            return False
        
    def check_funds (self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def __str__(self):
        output = ''
        line1 = self.name.center(30, "*")
        output += line1 + '\n'
        for items in self.ledger:
            # get values from "amount" : amount, "description" : description ledger list
            item = list(items.values())
            value = item[0]
            value = str('%.2f'%value)[: 7].rjust(7)
            name = item[1][: 23].ljust(23)
            output += name + value + "\n"
        output += "Total: " + str('%.2f'%self.get_balance())
        return output

              

def create_spend_chart(categories):
    line1 = 'Percentage spent by category'
    every_spent = list()
    cat_name = list()
    for category in categories:
        total_spent = 0
        for items in category.ledger:
            spent = list(items.values())
            if float(spent[0]) < 0:
                total_spent += spent[0]
        every_spent.append(total_spent)
        cat_name.append(category.name)

    total = sum(every_spent)
    percentage = list()
    for single_spent in every_spent:
        percentage.append(round(single_spent*100/total))

    output = line1 + '\n'
    temp = 100
    while temp >= 0:
        output += str(temp).rjust(3) + '|'
        for perc in percentage:
            if perc >= temp:
                output += ' o '
            else:
                output+= '   '
        temp = temp - 10
        output +=' '+'\n'
    dashes = ('-' * 3 * len(categories) + '-')
    output += dashes.rjust(3*len(categories)+5) + '\n'

    z = 0
    for x in range(len(max(cat_name, key = len))):
        output += '    '
        for name in cat_name:
            if x != z:
                output = output.rstrip() + '  ' + '\n' + '    '
                z += 1
            try:
                output +=' ' + name[x] + ' '
            except:
                output +='   '
    output = output.rstrip() + '  '
    return(output)
