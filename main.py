from empirique import *
from analytique import *
lam = 2
mu = 1.5
k = 8
x = []
Ly = []
simLy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(lam, mu, i, k, 10000)
	quSim.simRun()
	simLy.append(quSim.avgWaitLen)
	Ly.append(L_(lam, mu, i, k))
print ("L")
print(Ly)
print(simLy)
x = []
Wy = []
simWy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(lam, mu, i, k, 10000)
	quSim.simRun()
	simWy.append(quSim.avgWaitTime)
	Wy.append(W_(lam, mu, i, k)*60)
print ("W")
print(Wy)
print(simWy)
mu = 6.0
s = 2
k = 8
x = []
Lqy = []
simLqy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(i, mu, s, k, 10000)
	quSim.simRun()
	simLqy.append(quSim.avgWaitQuLen)
	Lqy.append(Lq(i, mu, s, k))
print("Lq")
print(Lqy)
print(simLqy)
Wqy = []
simWqy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(i, mu, s, k, 100000)
	quSim.simRun()
	simWqy.append(quSim.avgWaitQuTime)
	Wqy.append(Wq(i, mu, s, k)*60)
print("wq")
print(Wqy)
print(simWqy)