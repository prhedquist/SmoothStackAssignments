def BMI(num):
    count = 0
    bmiList = []
    while count < num:
        weight = int(input('Please enter weight: '))
        height = round(float(input('Please enter height: ')), 2)
        BMI = weight/(height**2)
        if BMI < 18.5:
            bmiList.append('under')
        elif BMI >= 18.5 and BMI < 25:
            bmiList.append('normal')
        elif BMI >= 25 and BMI < 30:
            bmiList.append('over')
        else:
            bmiList.append('obese')
        count += 1
    return bmiList


print(BMI(3))