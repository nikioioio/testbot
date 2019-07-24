import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        'cb5392c35661370d95f300086accea51/raw/'
        '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
        'indicators.csv')
t = df[df['Year'] ==int(1957)]
t1 = t.groupby('Country Name')['Value'].mean()[:10]
dt = pd.DataFrame(t1)
    # x = [{} for x in range(len(t1))]
    # print(x)

fig, ax = plt.subplots()

ax.bar([x for x in range(len(t1))], [y for y in t1])
ax.set_xticks(np.arange(len(t1)))
labels = [x for x in t1.index]
print(labels)
ax.set_xticklabels(labels,rotation = 90)


# plt.show()

plt.savefig('foo.png')
plt.close()