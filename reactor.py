      #1 checking if the reactor is criticality balanced
def is_criticality_balanced(temperature, neutrons):
    if(temperature < 800 and neutrons > 500 and (temperature * neutrons < 500000)):
        return True
    else:
        return False
    #2 checking the reactor efficiency
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power)*100
    if efficiency >= 80:
        return "GREEN"
    elif  80 > efficiency >= 60:
        return "ORANGE"
    elif 60 > efficiency >= 30:
        return "RED"
    else:
        return "BLACK"
    #3 mechanism against reactor overload and meltdown
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    reactor_output = temperature * neutrons_produced_per_second
    lower_bound = threshold * 0.9
    upper_bound = threshold * 1.1
    if reactor_output < lower_bound:
        return "LOW"
    elif lower_bound <= reactor_output <= upper_bound:
        return "NORMAL"
    else:
        return "TOO HIGH"

#1a
result = is_criticality_balanced(950, 600)
print(result)
#2
result = reactor_efficiency(120,6,160)
print(result)
#3
result = fail_safe(10, 200, 100)
print(result)
