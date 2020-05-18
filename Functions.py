# Create problem 
prob = LpProblem("Mixed products", LpMaximize)

#days 
Investment_1 = LpVariable("Investment_1", cat=LpInteger, lowBound=0)   
Investment_2 = LpVariable("Investment_2", cat=LpInteger, lowBound=0)
Investment_3 = LpVariable("Investment_3", cat=LpInteger, lowBound=0)   
Investment_4 = LpVariable("Investment_4", cat=LpInteger, lowBound=0)
Investment_5 = LpVariable("Investment_5", cat=LpInteger, lowBound=0)

# Objective Function:
## Profit
prob += Investment_5 * 2


# Constraints: 
## Recipes for products (R & E should appear together in one constraint, otherwise you can use the same amount units in multiple bottles)
prob += Investment_1 + Investment_2*0 + Investment_3*0 + Investment_4*0 + Investment_5*0   <= (2/3)*100
prob += Investment_1*(3/2) + Investment_2 + Investment_3*0 + Investment_4*0 + Investment_5*0 <= 100
prob += -Investment_1*(1/2) + Investment_2*(3/2) + Investment_3 + Investment_4*0 + Investment_5*0 <= 100
prob += -Investment_1*(1/2) - Investment_2*(1/2) + Investment_3*(3/2) + Investment_4 + Investment_5*0 <= 100
prob += -Investment_1*(1/2) - Investment_2*(1/2) - Investment_3*(1/2) + Investment_4*(3/2) + Investment_5 <= 100
prob += -Investment_1*(1/2) - Investment_2*(1/2) - Investment_3*(1/2) - Investment_4*(1/2) + Investment_5*(3/2) <= 100
prob += -Investment_1*(1/2) - Investment_2*(1/2) - Investment_3*(1/2) - Investment_4*(1/2) - Investment_5*(1/2) <= 100




print(prob)

status = prob.solve()    # Solver 
print(LpStatus[status])   # The solution status 
  
# Printing the final solution 
print(value(Investment_1), value(Investment_2), value(Investment_3), value(Investment_4), value(Investment_5) ,  value(prob.objective))
