from pygal_die.die import Die
import pygal

die6_1 = Die(6)
die6_2 = Die(6)

results = []

for roll_num in range(1000):
    result = die6_1.roll() + die6_2.roll()
    results.append(result)

    frequencies = []

print(results)

max_num_sides = die6_1.num_sides + die6_2.num_sides
for value in range(2, max_num_sides+1):
    frequence = results.count(value)
    frequencies.append(frequence)

print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(2,13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
