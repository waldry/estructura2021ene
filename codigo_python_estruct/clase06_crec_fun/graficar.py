# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = []
# corresponding y axis values
y = []

arr = [
    (54000, 0.06056504249572754, 0.0069590654130232054),
    (56000, 0.07555673122406006, 0.01695597013226414),
    (58000, 0.07135913372039795, 0.009036559986590677),
    (60000, 0.06866283416748047, 0.007266463155621284),
    (62000, 0.08734748363494874, 0.025992163751643243),
    (64000, 0.07755551338195801, 0.008496705817205259),
    (66000, 0.08495137691497803, 0.02065499499880134),
    (68000, 0.10793797969818116, 0.033908660571593016),
    (70000, 0.10464015007019042, 0.01583029873917339),
    (72000, 0.15641026496887206, 0.06399648354139058),
    (74000, 0.1362217903137207, 0.03104840621277381),
    (76000, 0.13052492141723632, 0.036439943779775705),
    (78000, 0.15011396408081054, 0.02786711372539829),
    (80000, 0.13232407569885254, 0.0134332752277437),
    (82000, 0.12173023223876953, 0.013887890652557135),
    (84000, 0.13292372226715088, 0.011900181904118696),
    (86000, 0.14311788082122803, 0.013027387091124741),
    (88000, 0.14891471862792968, 0.016641581970164382),
    (90000, 0.14901416301727294, 0.02503801499281876),
    (92000, 0.1618072509765625, 0.03380987959215508),
    (94000, 0.16490526199340821, 0.02618508605969981),
    (96000, 0.19158999919891356, 0.04037525044096745),
    (98000, 0.17290091514587402, 0.01442134862964167),
]

for i, j, k in arr:
    x.append(i)
    y.append(j)


# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
