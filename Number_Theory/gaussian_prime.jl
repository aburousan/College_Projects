### A Pluto.jl notebook ###
# v0.14.4

using Markdown
using InteractiveUtils

# ╔═╡ 5eace151-4b1c-41c5-ba0f-85651382056d
begin
	import Pkg
	Pkg.add("PlutoUI")
	Pkg.add("ImageTransformations")
	Pkg.add("TestImages")
end

# ╔═╡ 7724044a-6503-4ef8-b1f8-9d9794f2d6b7
begin
	using Primes
	using Plots#We are also calling this as we will plot the results.
	using PlutoUI#To see some output beautifully
end

# ╔═╡ 53e59472-5eed-4388-bf9f-30219716abf7
begin
	using Images
	problem = load("problem.jpeg")
end

# ╔═╡ f6758a16-7cdf-4399-a078-0d5c05d3c2a6
begin
	using ImageTransformations
	hand_drawn = load("img2.jpg")
	img = imresize(hand_drawn,ratio=1/10)
end

# ╔═╡ 1a288096-8885-4ad2-9c1f-3d55283cc92e
md"""
# Gaussian Prime Spiral
#### Author: Kazi Abu Rousan
We all know about complex numbers right?, They are of the form $z=a+bi$, were $i=\sqrt{-1}$. They are nothing fancy. They simply represent points in our good old coordinate plane. Like $z=a+bi$ represent the point $(a,b)$.
"""

# ╔═╡ ce8ae45c-e65f-4075-9114-99dbc14874ce
md"""
In $\textbf{Julia programming Language}$, we represent $i=\sqrt{-1}$ as "$\textbf{im}$". So, $z=a+bi$ is written as $\textit{a+b*im}$.
 As can example,
"""

# ╔═╡ f96fe032-a854-11eb-0da8-21a09cb2c5fc
z = 1+2im

# ╔═╡ 42cd7811-f699-474b-9f36-40f78024f27d
md"""
Real or Imaginary components of any $\textit{complex number}$ can be reached by using the command $\textbf{real()}$ or $\textbf{imag()}$ respectively. As an example,
"""

# ╔═╡ ce082035-9d84-4336-9eb0-c3c6b93a8069
real(z)

# ╔═╡ 455ecb41-bca7-4d83-bb8b-15829516f8de
imag(z)

# ╔═╡ d16b93e3-4506-4db7-9a35-e1665d3d9430
md"""
The absolute value can be found using the command $\textbf{abs()}$ and the square of the absolute value can also be found by $\textbf{abs2()}$. As an example,
"""

# ╔═╡ e5cea65a-6422-4778-a477-c2e3bbaf1738
abs(z)

# ╔═╡ 58cabae7-6366-4983-a4af-3b103013e686
abs2(z)

# ╔═╡ 654167c9-3d5d-49d7-8110-d11f80b8bb96
md"""
To plot $\textbf{Gaussian prime spiral}$, we have to first understand what is a $\textbf{gaussian prime}$ and how to find one. They are actually a special type of $\textbf{gaussian integers}$(complex numbers with $\textit{integer real and imaginary component}$). The gaussian integers which doesn't have any factor in the complex field are called $\textbf{gaussian prime}$.
"""

# ╔═╡ 29e1a13a-c777-4b85-9a8c-f7988db182f3
md"""
Like $5+3i$ can be factorised as $(1+i)(3-2i)$. So, It is not a $\textbf{gaussian prime}$. But $3-2i$ is a $\textbf{gaussian prime}$ as it cannot be further factorised. Likewise, 5 can be factorised as $(2+i)(2-i)$ so it is not a gaussian prime. But 3 is gaussian prime as it cannot be further factorised. Hence, $\textbf{3+0i}$ is a $\textbf{gaussian prime}$.
"""

# ╔═╡ beeb4ee1-ed9f-4ae0-88e5-9c5c649ca56a
md"""
To find if a number is gaussian prime or not, we will use 2 rules:
"""

# ╔═╡ 590a35ae-af84-4b26-adac-caae68417084
md"""
1. If the real or imaginary component if the given number is zero, then if the other one is a prime of form $4n+3$, then It will be a gaussian prime. As an example, $5+0i$ is a gaussian prime as although it's real component is zero, it is not of the form $4n+3$. But $3i$ is a $\textbf{gaussian prime}$, as it's real component is zero and $im(3i)=3$ is a prime of form $4n+3$.
2. If both real and imaginary components of a number $z=a+bi$ are non-zero, then we calculate $abs2=a^2+b^2$. If abs is a prime, then it is a gaussian prime. This prime will be of form $4n+1$(from fermat's two square theorem).
"""

# ╔═╡ 9e5a1bec-e290-42e5-81fa-91b2efc2a0a4
md"""
Using this 2 points, we will write a function to check if any given number is gaussian prime or not. To check if any number is normal real prime(eg: 2,3,1033,...), we will use the $\textbf{isprime}$ function $\textbf{Primes}$ package. This returns true or false based upon the number given. Eg: $\textbf{isprime(3)}$ > true ; $\textbf{isprime(10)}$ > false.
"""

# ╔═╡ 2624067b-2f3d-4793-90b5-fb112c04100a
function gaussian(z)#Function to check gaussian prime or not.
	ima = abs(imag(z)); rea = abs(real(z))
	if z == 0
		return false
	elseif rea != 0 && ima != 0
		d = abs2(z)
		return isprime(d)
	elseif rea == 0 || ima == 0
		mod_z = abs(z) |> Int
		if mod(mod_z,4) == 3
			return isprime(mod_z)
		else
			return false
		end
	end
end	

# ╔═╡ d6739510-517c-48e6-907a-44c58366f590
md"""
Now, Lets's see if our code is working well or not. To check output use wikipidia list or any other list as the correct value.
"""

# ╔═╡ 4fdf1b66-a20e-4771-9235-2735120a6874
gaussian(5)

# ╔═╡ 94a57e30-d0ee-48e3-83db-7ec3fce19184
gaussian(4+5im)

# ╔═╡ 526a6a6c-dd88-40db-8f40-4788ef704afe
md"""
Now, let's plot all the gaussian primes in the range of $10$ to $-10$ and $10i$ to $-10i$.
"""

# ╔═╡ 5503546f-1146-4270-951e-5495ce3e6999
function gaussian_prime_inrange(n::Int64)#Find gaussian prime in a circle of radius n
	list = Complex{Int64}[]
	for a = -n:n , b = -n:n
		gaussian_int = a + b*im
		push!(list,gaussian_int)
	end
	return filter(gaussian, list)
end

# ╔═╡ d2a3e7a4-4626-40f2-b088-d45b23642303
gaussain_array = gaussian_prime_inrange(50)

# ╔═╡ 74bf242c-e8f6-4722-8ab9-580aa115b677
begin
	scatter((gaussain_array), color=:red,markersize=3,size=(450,450),
	title="Gaussian primes",framestyle= :origin,label="Gaussian Primes")
end

# ╔═╡ 4b0900ad-9c9b-4320-90de-185d323191d0
md"""
Now, we are ready to solve a particular problem. Let's see what is it:(The problem is taken from $\textbf{Learning Scientific Programming with Python}$, 2nd edition, written by $\textbf{Christian Hill}$.)
"""

# ╔═╡ 6e4801be-1057-4f52-b0c7-eb19ee37c1e8
md"""
I have already solved it using python. The output should be something like this:
"""

# ╔═╡ 663acf07-1caa-4b3b-bf2c-55c2b923cbb9
begin
	solution = load("solution.png")
	sol = imresize(solution,ratio=1/1.2)
end

# ╔═╡ 518a0b4b-2890-4396-93a7-1dd7a6c0967f
md"""
Let's see how to draw the spiral for a initial point $c_0=3+2i$ and $\Delta c = 1+0i=1$.
"""

# ╔═╡ 9c2ab114-b3ef-465a-98c2-f112f4a9979c
md"""
1. For the first step, we don't care if $c_0$ is $\textbf{gaussian prime}$ or not. We just add the step with it, i.e., we add $\Delta c$ with $c_0$. For our case it will give us $c_1=(3+2i)+1=4+2i$.
2. Then, we check if $c_1$ is a $\textbf{gaussian prime}$ or not. In our case, $c_1=4+2i$ is not a gaussian prime. So, we repeat step 1(i.e., add $\Delta c$ with it). This gives us $c_2=5+2i$. Again we check if $c_2$ is gaussian prime or not. In this case, $c_2$ $\textbf{is a gaussian prime}$. So, now we have to $\textbf{rotate the direction}$ $90^{\circ}$ $\textbf{towards the left}$,i.e., anti-clockwise. In complex plane, it is very easy. Just multiply the $\Delta c$  by  $i = \sqrt{-1}$ and that will be our new $\Delta c$. For our example, $c_3=c_2+\Delta c=5+2i+(1+0i)\cdot i=5+3i$.
3. From here, again we follow step-2, until we get the point from where we started with the same $\Delta c$ or you can do it for your required step.
"""

# ╔═╡ a55105e1-75d5-4f46-98ff-01b1df38d509
md"""
Here is a hand drawn $\textbf{gaussian spiral}$ for 4 steps.
"""

# ╔═╡ 2f83b5e0-4f2c-4482-8267-2e142a2e7f2e
md"""
Now, let's write a program to draw these spirals.
"""

# ╔═╡ 2704643a-c0a7-41e4-a3ea-bcc4e08b39ba
begin
	seed = 3+2*im; Δc = 1; step = 0; d = seed
	prime_list = ComplexF64[]; points = ComplexF64[seed]
	for i in 1:30
		seed = seed + Δc; step += 1
		push!(points,seed)
		if gaussian(seed)
			Δc = Δc*im
			push!(prime_list,seed)
		end
	end
end

# ╔═╡ d0d5b574-34b3-4df9-a8fb-0f384b619a0d
with_terminal() do#I have given this just to show you a method to use terminal
	println(points)
end

# ╔═╡ 16cd0ac9-f169-4518-96b7-9278091e747a
md"""
This is the program to plot spiral. Here I have used $\textbf{for loop}$ to just calculate for 30 steps. Here i have printed all the values, we get by following the step1 and step2  30 times.
"""

# ╔═╡ 3f481b21-67ae-48fa-b960-f741a32d0a66
md"""
Let's plot this. Remember the initial point is $3+2i$.
"""

# ╔═╡ 198f57f3-4f69-4089-a205-f77d4b5e50e0
begin
	plot((points),color=:blue,width=3,title="Gaussian prime Spiral",label="spiral",framestyle= :origin,size=(560,560))
	scatter!((points),color=:green,label="Gaussian Integers");scatter!((prime_list),label="Gaussian primes",color=:Red)
	xlabel!("Re(z) ; steps = $step and C0 = $d"); ylabel!("Im(z)")
	
end

# ╔═╡ 25bf9ea8-c8db-475a-a827-ef6113f3e45a
md"""
Now, Let's define the plotting block of code as a function. That function can plot number of steps according to your wish or it can plot until it returns to it's starting state (i.e., $\Delta c=1$ and starting value of $c_0$).
"""

# ╔═╡ e6802038-b329-409e-b76a-9244551cd360
function gaussian_spiral(seed;loop_num=1,Δc=1,initial_con = true)
	d = seed; points = Complex{Int64}[d]
	if initial_con
		while true
			seed += Δc
			push!(points,seed)
			if seed == d
				break
			end
			if gaussian(seed)
				Δc = Δc*im
			end
		end
	else
		for i in 1:loop_num
			seed += Δc
			push!(points,seed)
			if gaussian(seed)
				Δc = Δc*im
			end
		end
	end
	prime_list = filter(gaussian,points)
	return points, prime_list
end

# ╔═╡ fbdc650a-d377-4215-9788-a7964ec7e836
begin
	point, primes = gaussian_spiral(5+23*im)
	step_count = size(point)[1] - 1
	start = point[1]
end

# ╔═╡ 6f4d97e7-4c90-4795-bea3-11f75a1186b0
md"""
So, We have all the data in the 3 variables.
1. points = Contains all $\textbf{Gaussian integers}$, which will create our spiral.
2. primes = Contains all $\textbf{Gaussian primes}$, which are generated in the process.
3. step_count = which contains the number of steps needed for a particular spiral.
"""

# ╔═╡ 5a409e7c-978b-4cc9-88ef-aa07a589d883
begin
	plot((point),color=:blue,width=3,title="Gaussian prime Spiral",label="spiral",framestyle= :origin,size=(650,650))
	scatter!((primes),label="Gaussian primes",color=:Red)
	xlabel!("Re(z) ; steps = $step_count and C0 = $start"); ylabel!("Im(z)")
	
end

# ╔═╡ 208b5fe6-4b72-415f-a03b-5d46fb641107
md"""
Too beautiful!, Let's plot few more.
"""

# ╔═╡ 70e59589-c443-4aa4-ae82-79788b9d97df
begin
	point1, prime1 = gaussian_spiral(60+im)
	step_count1 = size(point1)[1] - 1
	start1 = point1[1]
end

# ╔═╡ 3f458c3f-3355-4436-91e2-3baee11a0165
md"""
Now, Let's plot it.
"""

# ╔═╡ 5c725f63-1a52-47fe-a8ae-0f8bfc62b63d
begin
	plot((point1),color=:blue3,width=2.4,title="Gaussian prime Spiral",label="spiral",framestyle= :origin,size=(660,660))
	scatter!((prime1),label="Gaussian primes",color=:Red,markersize=3.32,markerstrokewidth = 0)
	xlabel!("Re(z) ; steps = $step_count1 and C0 = $start1"); ylabel!("Im(z)")
	
end

# ╔═╡ eda83470-daa8-429d-9b44-41061dd7b88c
md""""
If you don't like change the colour or maybe remove the gaussian primes.
"""

# ╔═╡ de1fe555-8b4f-45c7-b65b-ace24033c86e
md"""
Last one 

"""

# ╔═╡ 20cc55a9-800a-41fa-8871-69b531ae3e1e
begin
	point2, prime2 = gaussian_spiral(277+232*im)
	step_count2 = size(point2)[1]-1
	start2 = point2[1]
end

# ╔═╡ e3892073-60fd-4789-a9e2-76d1f35f9ec0
begin
	plot((point2),color=:blue3,width=2.4,title="Gaussian prime Spiral",label="spiral",framestyle= :origin)
	scatter!((prime2),label="Gaussian primes",color=:Red,markersize=0.1,markerstrokewidth = 0)
	xlabel!("Re(z) ; steps = $step_count2 and C0 = $start2"); ylabel!("Im(z)")
	
end

# ╔═╡ 377ae8b0-ddd1-4b7f-b427-3b4286c0894c
md"""
Damn!!...It's too beautiful. I am just a beginner in $\textbf{julia}$ so, the graphs are still not that good. Here is the same plot in $\textbf{python}$.
"""

# ╔═╡ 8a35ca32-7bf7-4abd-9bd1-c94e131a5062
begin
	finall = load("img5.png")
	final = imresize(finall,ratio=1/2)
end

# ╔═╡ a493df57-9058-45f9-9804-2a9ff889fab4
md"""
😳 Am I seeing Batman doing back-flip?
"""

# ╔═╡ Cell order:
# ╟─1a288096-8885-4ad2-9c1f-3d55283cc92e
# ╟─5eace151-4b1c-41c5-ba0f-85651382056d
# ╟─ce8ae45c-e65f-4075-9114-99dbc14874ce
# ╠═f96fe032-a854-11eb-0da8-21a09cb2c5fc
# ╟─42cd7811-f699-474b-9f36-40f78024f27d
# ╠═ce082035-9d84-4336-9eb0-c3c6b93a8069
# ╠═455ecb41-bca7-4d83-bb8b-15829516f8de
# ╟─d16b93e3-4506-4db7-9a35-e1665d3d9430
# ╠═e5cea65a-6422-4778-a477-c2e3bbaf1738
# ╠═58cabae7-6366-4983-a4af-3b103013e686
# ╟─654167c9-3d5d-49d7-8110-d11f80b8bb96
# ╟─29e1a13a-c777-4b85-9a8c-f7988db182f3
# ╟─beeb4ee1-ed9f-4ae0-88e5-9c5c649ca56a
# ╟─590a35ae-af84-4b26-adac-caae68417084
# ╟─9e5a1bec-e290-42e5-81fa-91b2efc2a0a4
# ╠═7724044a-6503-4ef8-b1f8-9d9794f2d6b7
# ╠═2624067b-2f3d-4793-90b5-fb112c04100a
# ╟─d6739510-517c-48e6-907a-44c58366f590
# ╠═4fdf1b66-a20e-4771-9235-2735120a6874
# ╠═94a57e30-d0ee-48e3-83db-7ec3fce19184
# ╟─526a6a6c-dd88-40db-8f40-4788ef704afe
# ╠═5503546f-1146-4270-951e-5495ce3e6999
# ╠═d2a3e7a4-4626-40f2-b088-d45b23642303
# ╠═74bf242c-e8f6-4722-8ab9-580aa115b677
# ╟─4b0900ad-9c9b-4320-90de-185d323191d0
# ╟─53e59472-5eed-4388-bf9f-30219716abf7
# ╟─6e4801be-1057-4f52-b0c7-eb19ee37c1e8
# ╟─663acf07-1caa-4b3b-bf2c-55c2b923cbb9
# ╟─518a0b4b-2890-4396-93a7-1dd7a6c0967f
# ╟─9c2ab114-b3ef-465a-98c2-f112f4a9979c
# ╟─a55105e1-75d5-4f46-98ff-01b1df38d509
# ╟─f6758a16-7cdf-4399-a078-0d5c05d3c2a6
# ╟─2f83b5e0-4f2c-4482-8267-2e142a2e7f2e
# ╠═2704643a-c0a7-41e4-a3ea-bcc4e08b39ba
# ╠═d0d5b574-34b3-4df9-a8fb-0f384b619a0d
# ╟─16cd0ac9-f169-4518-96b7-9278091e747a
# ╟─3f481b21-67ae-48fa-b960-f741a32d0a66
# ╠═198f57f3-4f69-4089-a205-f77d4b5e50e0
# ╟─25bf9ea8-c8db-475a-a827-ef6113f3e45a
# ╠═e6802038-b329-409e-b76a-9244551cd360
# ╠═fbdc650a-d377-4215-9788-a7964ec7e836
# ╟─6f4d97e7-4c90-4795-bea3-11f75a1186b0
# ╠═5a409e7c-978b-4cc9-88ef-aa07a589d883
# ╟─208b5fe6-4b72-415f-a03b-5d46fb641107
# ╠═70e59589-c443-4aa4-ae82-79788b9d97df
# ╟─3f458c3f-3355-4436-91e2-3baee11a0165
# ╠═5c725f63-1a52-47fe-a8ae-0f8bfc62b63d
# ╟─eda83470-daa8-429d-9b44-41061dd7b88c
# ╟─de1fe555-8b4f-45c7-b65b-ace24033c86e
# ╠═20cc55a9-800a-41fa-8871-69b531ae3e1e
# ╠═e3892073-60fd-4789-a9e2-76d1f35f9ec0
# ╟─377ae8b0-ddd1-4b7f-b427-3b4286c0894c
# ╟─8a35ca32-7bf7-4abd-9bd1-c94e131a5062
# ╟─a493df57-9058-45f9-9804-2a9ff889fab4
