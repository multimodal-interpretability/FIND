import torch
import torch.nn as nn
import sys
import os
dir_path = os.path.dirname(os.path.abspath(__file__))

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

def function(x):
    model = MLP()
    model.load_state_dict(torch.load(os.path.join(dir_path, 'mlp_approx_model.pt')))
    model.eval()
    return model(torch.tensor(x).reshape(-1, 1).float()).item()

if __name__ == '__main__':
    outputs = ''
    for arg in sys.argv[1:]:
        x = float(arg)
        outputs += f'({arg}, {str(function(x))}) '
    print(f'Function input - output pairs: {outputs}')