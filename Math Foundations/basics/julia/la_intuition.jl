using LinearAlgebra

println("=== Vectors ===")
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

println("a = ", a)
println("b = ", b)
println("a + b = ", a + b)
println("a - b = ", a - b)
println("a * 3 = ", a * 3)
println("a · b = ", a ⋅ b)
println("|a| = ", norm(a))
println("â = ", normalize(a))

cosine = (a ⋅ b) / (norm(a) * norm(b))
println("cosine_similarity(a, b) = ", round(cosine, digits=4))

println("\n=== Matrices ===")
rotation_90 = [0 -1; 1 0]
point = [3.0, 1.0]
rotated = rotation_90 * point
println("matrix of rotation: ", rotation_90)
println("Rotate the point: ", point, " by 90° → ", rotated)

println("\n=== Neural Network Layer ===")
W = randn(2, 3) * 0.1
x = [1.0, 0.5, -0.3]
output = W * x
println("Input (3D):  ", x)
println("Output (2D): ", output)
println("^ This is literally what a neural network layer does.")
#=
=== Vectors ===
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
a + b = [5.0, 7.0, 9.0]
a - b = [-3.0, -3.0, -3.0]
a * 3 = [3.0, 6.0, 9.0]
a · b = 32.0
|a| = 3.7416573867739413      
â = [0.2672612419124244, 0.5345224838248488, 0.8017837257372732]          
cosine_similarity(a, b) = 0.9746
=== Matrices ===
matrix of rotation: [0 -1; 1 0]
Rotate the vector[3.0, 1.0] by 90° gives → [-1.0, 3.0]
=== Neural Network Layer ===
Input (3D) x:  [1.0, 0.5, -0.3]
the matrix W: [0.058825311672097515 0.1003128455987768 -0.04285498638821025; 0.055801956224288934 -0.0288708877953867 -0.07701367209458806]
Output (2D) W*x: [0.121838230387949, 0.064470613954972]
^ This is literally what a neural network layer does.


=#
