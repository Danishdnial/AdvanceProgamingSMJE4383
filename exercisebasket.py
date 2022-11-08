# take number of points one team is ahead
points_str = input ("Enter the lead in points:")
points_remaining_int = int(points_str)

# subtract three
lead_calculation_float= float(points_remaining_int-3)

# add half-point if the team that is ahead has the ball,
# and subtract a half_point if the other team has the ball
has_ball_str = input("Does the lead team has the ball? (Yes,No)")

if has_ball_str=="Yes":
    lead_calculation_float= lead_calculation_float+0.5
else:
    lead_calculation_float= lead_calculation_float-0.5
# numbers less than zero becomes zero
if lead_calculation_float<0:
    lead_calculation_float=0
# square that
lead_calculation_float= lead_calculation_float**2
# if the results are greater than the number of seconds left, the lead is safe
secods_remaining_int= int(input('Enter the number of seconds remaining:'))
if lead_calculation_float> secods_remaining_int:
    print('Lead is safe!')
else:
    print('Lead is not safe!')