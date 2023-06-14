import pdb

import torch
import torch.nn as nn
import torch.optim as optim
import os
import math_functions as mf
import matplotlib.pyplot as plt
from utils import timer_decorator


# Define our MLP model
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(1, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.layers(x)

@timer_decorator
def train_function(x, f, func_name, x_test, dirname, verbose=False):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    y = f(x)

    x = torch.tensor(x, dtype=torch.float32).to(device)
    y = torch.tensor(y, dtype=torch.float32).to(device)

    # Initialize the model, loss function and optimizer
    model = MLP().to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # Train the model
    model.train()
    epochs = 10000
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        if verbose and epoch % 1000 == 0:
            print(f'Epoch: {epoch}, Loss: {loss.item()}')

    if verbose:
        print("Training complete.")
    y_test = torch.tensor(f(x_test), dtype=torch.float32).to(device)
    x_test = torch.tensor(x_test, dtype=torch.float32).to(device)
    y_pred = model(x_test)
    # Test the model with some input
    loss = criterion(y_pred, y_test)
    torch.save(model.state_dict(), f'{dirname}/mlp_approx_model.pt')

    # plot the result in a figure with two subplots
    plt.subplot(3, 1, 1)
    # plt.tight_layout()
    plt.plot(x.cpu(), y.cpu(), label='real')
    plt.title('Real function')
    plt.subplot(3, 1, 2)
    plt.plot(x.cpu(), model(x).detach().cpu().numpy(), label='predicted')
    plt.title('Predicted function')
    plt.subplot(3, 1, 3)
    plt.plot(x.cpu(), y.cpu(), label='real')
    plt.plot(x.cpu(), model(x).detach().cpu().numpy(), label='predicted')
    plt.savefig(f'{dirname}/mlp_approx_plot.png')
    plt.close()
    return loss.item()





