import torch
#Add dot product calculation using PyTorch
x = torch.randn(3, requires_grad=True)
y = torch.tensor([1.0, 0.0, 0.0])

similarity = torch.dot(x, y)
similarity.backward()

print(f"x = {x.data}")
print(f"y = {y.data}")
print(f"dot product = {similarity.item():.4f}")
print(f"d(dot)/dx = {x.grad}")
'''
x = tensor([-0.2494, -0.9554,  0.7208])
y = tensor([1., 0., 0.])
dot product = -0.2494
d(dot)/dx = tensor([1., 0., 0.])
'''

'''
comparaison between Numpy  & Torch
x=np.array([-0.2494, -0.9554,  0.7208])
y=np.array([1., 0., 0.])
np.dot(x,y) => -0.2494 == torch.dot(x, y)
'''
