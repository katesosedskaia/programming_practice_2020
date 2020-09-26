#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
def y(x):
    f=np.log(np.e**(1/(np.sin(x)+1))/(5/4+1/x**15)) / np.log(1+x**2)
    return f
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
    print(y(a[i]))


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.plot(x, x**2-x-6 )
plt.show()


# In[7]:


import numpy as np
import matplotlib.pyplot as plt
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.log((x**2+1)*np.exp(-np.abs(x)/10))/np.log(1+np.tan(1/(1+(np.sin(x))**2))))
plt.show()


# In[11]:


a=input()
plt.plot([eval(a) for x in range (100)])


# In[15]:


with plt.xkcd():
    plt.pie([40, 25, 10, 15, 10], labels=('ФБМФ', 'ФЭФМ', 'ФПМИ','ФАКТ','ФРКТ'))
    plt.title('Процент девушек в различных Физтех-школах')



# In[62]:


import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
p, v = np.polyfit(x, y, deg=2, cov=True)
d, f = np.polyfit(x, y, deg=1, cov=True)
print(p)
print(d)
a= np.arange(1, 5.01, 0.01)
sp = plt.subplot(121)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
k=np.poly1d(p)
plt.plot(a, k(a))
sp = plt.subplot(122)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
q=np.poly1d(d)
plt.plot(a, q(a))




