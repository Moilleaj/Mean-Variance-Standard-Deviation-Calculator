import numpy as np

def calculate(list):
  if len(list) == 9:
    a = np.array(list).reshape(3,3)
    calculations = {'mean':[],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []}
    calculations['mean']+= np.mean(a, axis = 0).tolist(), np.mean(a, axis = 1).tolist(), np.mean(a)
    calculations['variance']+= np.var(a, axis = 0).tolist(), np.var(a, axis = 1).tolist(), np.var(a)
    calculations['standard deviation']+= np.std(a, axis = 0).tolist(), np.std(a, axis = 1).tolist(), np.std(a)
    calculations['max']+= np.max(a, axis = 0).tolist(), np.max(a, axis = 1).tolist(), np.max(a)
    calculations['min']+= np.min(a, axis = 0).tolist(), np.min(a, axis = 1).tolist(), np.min(a)
    calculations['sum']+= np.sum(a, axis = 0).tolist(), np.sum(a, axis = 1).tolist(), np.sum(a)
    return calculations
  else:
    raise ValueError('List must contain nine numbers.')