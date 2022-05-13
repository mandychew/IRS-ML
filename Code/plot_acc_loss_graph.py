import matplotlib.pyplot as plt

def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])

  dtime = dt.time()
  now = dt.datetime.now()
  now.strftime("%Y-%m-%d %H-%M-%S")

  plt.savefig(f'{now}.png')