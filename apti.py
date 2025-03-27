import random

def qb():
    global question1,select,d1,d2,d3,d4
    question1 = [
    "Find the missing number: 2, 6, 12, 20, ?",
    "A shopkeeper buys an article for ₹800 and sells it for ₹960. What is the profit percentage?",
    "A can complete a work in 10 days, and B can complete the same work in 15 days. If they work together, in how many days will they finish the work?",
    "A train 180 meters long is running at a speed of 90 km/h. How much time will it take to cross a pole?",
    "A sum of ₹5000 is invested at an interest rate of 6% per annum for 2 years. What is the simple interest?",
    "The present age of a father is three times the age of his son. After 10 years, the father’s age will be twice the son’s age. What is the present age of the son?",
    "Find the odd one out: 36, 49, 64, 100, 121, 133",
    "If TABLE is written as GZYOV, then how will CHAIR be written?",
    "Pointing to a man, Rahul said, 'He is the only son of my father's father.' How is the man related to Rahul?",
    "A bag contains 5 red, 4 green, and 3 blue balls. If one ball is drawn at random, what is the probability that it is not red?",
    # Number System
    "Find the greatest number that will divide 201, 311, and 421 leaving the same remainder.",
    "The product of two numbers is 2160, and their HCF is 12. Find their LCM.",
    "What is the remainder when 3456789 is divided by 9?",
    "Find the smallest number that should be added to 8931 to make it exactly divisible by 7.",
    "If 2x + 3y = 36 and x/y = 3/4, find the value of x and y.",
    
    # LCM & HCF
    "Find the LCM and HCF of 72, 108, and 180.",
    "The HCF of two numbers is 16, and their LCM is 192. If one of the numbers is 32, find the other number.",
    "Three bells ring at intervals of 8, 12, and 15 minutes. After how long will they ring together again?",
    "The sum of two numbers is 120, and their HCF is 6. Find the maximum LCM possible.",
    "The product of two numbers is 5040, and their LCM is 280. Find their HCF.",
    
    # Ratio & Proportion
    "If a:b = 5:7 and b:c = 3:8, find a:c.",
    "Two numbers are in the ratio 3:5. If their sum is 128, find the numbers.",
    "Divide 180 into three parts in the ratio 2:3:4.",
    "The incomes of A and B are in the ratio 4:5, and their expenses are in the ratio 7:9. If A saves ₹5000 and B saves ₹8000, find their incomes.",
    "A mixture contains milk and water in the ratio 4:1. How much water must be added to 40 liters of this mixture to make the ratio 2:1?",
    
    # Percentages
    "A number is increased by 20% and then decreased by 25%. Find the net percentage change.",
    "The population of a town increased by 10% in the first year and decreased by 5% in the second year. Find the net change in population.",
    "A student scores 60% in an exam. If he got 240 marks, find the total marks of the exam.",
    "The price of a commodity increases by 30%. How much should consumption be reduced to maintain the same expenditure?",
    "If A's salary is 25% more than B's salary, then B’s salary is what percent less than A’s salary?",
    
    # Profit & Loss
    "A shopkeeper gains 20% on selling a product for ₹600. Find the cost price.",
    "A person sells two articles for ₹5000 each, one at a profit of 20% and the other at a loss of 20%. Find the net gain or loss.",
    "If the cost price of 20 articles is equal to the selling price of 16 articles, find the profit percentage.",
    "A trader allows a discount of 10% on the marked price of ₹800. If he still gains 8%, find the cost price.",
    "A person sold a watch for ₹1800 at a 10% loss. What should be the selling price to make a profit of 5%?",
    
    # Time & Work
    "A can complete a task in 10 days, and B can do it in 15 days. How long will it take both to complete it together?",
    "A, B, and C can complete a task in 6, 8, and 12 days, respectively. How long will it take for all three to finish it together?",
    "A alone can do a job in 16 days. After working for 4 days, he is joined by B. Together, they finish the job in 6 more days. Find B’s efficiency.",
    "If 6 men can complete a work in 10 days, how many men are required to complete the same work in 5 days?",
    "A pump can fill a tank in 20 minutes, but a leak in the tank empties it in 30 minutes. How long will it take to fill the tank?",
    
    # Direction Sense
    "A person walks 10 meters north, then turns right and walks 5 meters, then again turns right and walks 10 meters. Finally, he turns left and walks 10 meters. How far is he from his starting point?",
    "A man walks 30 meters towards the north, then turns left and walks 40 meters, then again turns left and walks 30 meters. How far is he from the starting position?",
    "If a person moves 15 km east and then 8 km south, what is the shortest distance from the starting point?",
    "A man is facing west. He turns 90° clockwise and then 180° counterclockwise. Which direction is he facing now?",
    "Rahul starts from his home facing south. He walks 20 meters, turns left, walks 30 meters, turns right, and walks 10 meters. In which direction is he now facing?",
    
    # Blood Relation
    "Pointing to a man, Rohan said, 'He is the son of my grandfather's only son.' How is the man related to Rohan?",
    "A woman introduces a man as 'the only son of my father’s wife.' How is the man related to the woman?",
    "A is the sister of B. B is the mother of C. How is A related to C?",
    "If P is the brother of Q, Q is the sister of R, and R is the father of S, how is P related to S?",
    "Pointing to a photograph, Neha said, 'He is the father of my brother's only son.' How is the person in the photograph related to Neha?",
    
    # Compound Interest & Present Value
    "Find the compound interest on ₹10,000 at 8% per annum for 2 years.",
    "The present value of ₹15,000 due in 3 years at an interest rate of 5% per annum is?",
    "A sum of ₹5,000 becomes ₹6,050 in 2 years at compound interest. Find the rate of interest.",
    "In how many years will ₹4,000 become ₹5,832 at 10% per annum compound interest?",
    "The difference between the simple interest and compound interest on ₹8,000 at 6% per annum for 2 years is?",
    
    # Algebra
    "Solve for x: 3x + 5 = 2x + 15.",
    "If x^2 - 9x + 18 = 0, find the roots of the equation.",
    "The sum of two numbers is 40, and their product is 375. Find the numbers.",
    "If (x + 3)(x - 2) = x^2 + ax + b, find the values of a and b.",
    "Solve: 2x^2 - 3x - 2 = 0 using the quadratic formula.",
    
    # Geometry
    "Find the area of a triangle with base 10 cm and height 8 cm.",
    "The perimeter of a rectangle is 48 cm. If its length is 14 cm, find its width.",
    "The sum of the interior angles of a polygon is 1080°. Find the number of sides.",
    "The radius of a circle is 7 cm. Find its circumference.",
    "A right-angled triangle has sides 6 cm and 8 cm. Find the hypotenuse.",
    
    # Ratio & Proportion
    "The ratio of the ages of A and B is 4:5. After 6 years, their ratio becomes 5:6. Find their present ages.",
    "A sum of ₹560 is divided among A, B, and C in the ratio 2:3:4. Find the share of C.",
    "If 15 men can complete a work in 20 days, how many men are required to complete it in 10 days?",
    "A and B invested in a business in the ratio 3:5. If the total profit is ₹16000, find B’s share.",
    "The speeds of two cars are in the ratio 4:5. If the first car covers 200 km in 5 hours, how much time will the second car take to cover the same distance?"


]

    options1 = [
    ["A) 30", "B) 28", "C) 32", "D) 34"],
    ["A) 18%", "B) 20%", "C) 25%", "D) 30%"],
    ["A) 5 days", "B) 6 days", "C) 8 days", "D) 9 days"],
    ["A) 5 sec", "B) 6 sec", "C) 7.2 sec", "D) 8 sec"],
    ["A) ₹600", "B) ₹550", "C) ₹620", "D) ₹800"],
    ["A) 10 years", "B) 15 years", "C) 20 years", "D) 25 years"],
    ["A) 49", "B) 100", "C) 133", "D) 121"],
    ["A) XSZRI", "B) XZSRG", "C) XYSRG", "D) XZSRH"],
    ["A) Brother", "B) Uncle", "C) Father", "D) Grandfather"],
    ["A) 3/4", "B) 2/3", "C) 5/12", "D) 7/12"],

    # Number System

    ["10", "15", "20", "25"],  # Correct: 10
    ["150", "180", "220", "240"],  # Correct: 180
    ["0", "2", "3", "5"],  # Correct: 3
    ["2", "3", "5", "6"],  # Correct: 5
    ["x=12, y=8", "x=9, y=6", "x=10, y=7", "x=15, y=10"],  # Correct: x=12, y=8

    # LCM & HCF
    ["LCM=2160, HCF=12", "LCM=540, HCF=36", "LCM=1260, HCF=24", "LCM=360, HCF=18"],  # Correct: LCM=1080, HCF=36
    ["24", "36", "48", "64"],  # Correct: 24
    ["120 min", "240 min", "60 min", "90 min"],  # Correct: 120 min
    ["100", "120", "140", "160"],  # Correct: 120
    ["10", "15", "18", "25"],  # Correct: 18

    # Ratio & Proportion
    ["5:8", "15:56", "7:8", "5:12"],  # Correct: 15:56
    ["48, 80", "36, 92", "54, 74", "52, 76"],  # Correct: 48, 80
    ["40, 60, 80", "30, 60, 90", "50, 55, 75", "20, 40, 60"],  # Correct: 40, 60, 80
    ["₹20,000, ₹25,000", "₹24,000, ₹30,000", "₹28,000, ₹35,000", "₹32,000, ₹40,000"],  # Correct: ₹32,000, ₹40,000
    ["5 liters", "10 liters", "20 liters", "15 liters"],  # Correct: 10 liters

    # Percentages
    ["5% decrease", "10% decrease", "12% decrease", "15% decrease"],  # Correct: 10% decrease
    ["4.5% increase", "5.5% increase", "6% increase", "6.5% increase"],  # Correct: 4.5% increase
    ["350", "380", "400", "420"],  # Correct: 400
    ["23%", "25%", "30%", "35%"],  # Correct: 23%
    ["20%", "22%", "25%", "28%"],  # Correct: 20%

    # Profit & Loss
    ["₹400", "₹450", "₹500", "₹550"],  # Correct: ₹500
    ["No loss, no gain", "₹500 gain", "₹500 loss", "₹1000 loss"],  # Correct: No loss, no gain
    ["10%", "20%", "25%", "30%"],  # Correct: 25%
    ["₹650", "₹700", "₹725", "₹750"],  # Correct: ₹700
    ["₹1900", "₹2000", "₹2100", "₹2200"],  # Correct: ₹2100

    # Time & Work
    ["5 days", "6 days", "8 days", "7.5 days"],  # Correct: 6 days
    ["8", "10", "12", "6"],  # Correct: 12
    ["1/5", "1/6", "1/8", "1/10"],  # Correct: 1/6
    ["6", "8", "10", "12"],  # Correct: 12
    ["30 min", "35 min", "40 min", "50 min"],  # Correct: 40 min

    # Direction Sense
    ["5 meters", "10 meters", "15 meters", "20 meters"],  # Correct: 5 meters
    ["10 m", "20 m", "30 m", "40 m"],  # Correct: 40 m
    ["12 km", "17 km", "20 km", "23 km"],  # Correct: 17 km
    ["North", "South", "East", "West"],  # Correct: South
    ["North", "South", "East", "West"],  # Correct: East

    # Blood Relation
    ["Father", "Brother", "Uncle", "Cousin"],  # Correct: Brother
    ["Father", "Brother", "Husband", "Son"],  # Correct: Brother
    ["Mother", "Aunt", "Sister", "Grandmother"],  # Correct: Aunt
    ["Uncle", "Grandfather", "Father", "Brother"],  # Correct: Uncle
    ["Father", "Brother", "Son", "Uncle"],  # Correct: Father

    # Compound Interest & Present Value
    ["₹1600", "₹1664", "₹1800", "₹1920"],  # Correct: ₹1664
    ["₹12900", "₹13000", "₹13050", "₹13250"],  # Correct: ₹12900
    ["5%", "6%", "7%", "8%"],  # Correct: 10%
    ["4 years", "5 years", "6 years", "7 years"],  # Correct: 6 years
    ["₹20", "₹24", "₹28", "₹32"],  # Correct: ₹24

    # Algebra
    ["5", "7", "10", "15"],  # Correct: 10
    ["3, 6", "2, 9", "1, 8", "4, 5"],  # Correct: 3, 6
    ["10, 30", "15, 25", "20, 20", "12, 28"],  # Correct: 15, 25
    ["a=1, b=-6", "a=2, b=-3", "a=1, b=-2", "a=3, b=-1"],  # Correct: a=1, b=-2
    ["x=2, -1", "x=3, -2", "x=4, -3", "x=5, -4"],  # Correct: x=2, -1

    # Geometry
    ["40 cm²", "50 cm²", "60 cm²", "80 cm²"],  # Correct: 40 cm²
    ["5 cm", "6 cm", "7 cm", "8 cm"],  # Correct: 5 cm
    ["6", "7", "8", "9"],  # Correct: 8
    ["22 cm", "28 cm", "33 cm", "44 cm"],  # Correct: 44 cm
    ["9 cm", "10 cm", "11 cm", "12 cm"],  # Correct: 10 cm

    # Ratio & Proportion
    ["16, 20", "20, 25", "24, 30", "28, 35"],  # Correct: 24, 30
    ["₹120", "₹140", "₹160", "₹180"],  # Correct: ₹160
    ["25", "30", "35", "40"],  # Correct: 30
    ["₹6000", "₹8000", "₹10000", "₹12000"],  # Correct: ₹10000
    ["4 hours", "4.5 hours", "5 hours", "5.5 hours"]  # Correct: 5 hours




]

# Select a random question
    select = random.randint(0, len(question1) - 1)
    

# Get a shuffled list of options
    random.shuffle(options1[select])

# Extract four options randomly (since they are already shuffled, just pick all)
    d1, d2, d3, d4 = options1[select]

 

qb()

