import os
import sys
import collections
import torch
import numpy as np
from torch.autograd import Variable
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.models as models

import torch
from sklearn.datasets import load_boston #资料为boston房价资料，位于包sticik_learn中
#double_queue = collections.deque()


if __name__ == "__main__":
    double_queue = collections.deque()
    double_queue.append(1)
    double_queue.append(2)
    print(double_queue)
    double_queue.popleft()
    print(double_queue)
    print(len(double_queue))
    print()
    print(torch.__version__)
    print()
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(x)
    # print()
    # sub_ts = torch.from_numpy(x)
    # print(sub_ts)
    #
    boston = load_boston()
    boston_tensor = torch.from_numpy(boston.data)
    print(boston.data.shape)
    print(boston_tensor.size())
    print(boston_tensor[:2])
    print(boston_tensor[:10:5])
    print("test")