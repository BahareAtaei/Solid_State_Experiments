# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#---------------------

# import data
df = pd.read_csv(r"https://raw.githubusercontent.com/BahareAtaei/Solid_State_Experiments/refs/heads/main/Temperature_Dependence_of_Electrical_Resistance_of_Metals/Initial_Dataset.csv")
print("********** Initial Data **********")
print('')
print(df.info())
print('='*50)
print('')
#--------------------

# making new columns
df["T(K)"] = df["theta(degree)"] + 273.15
df["L2(cm)"] = 100 - df["L1(cm)"]
df["R(ohm)"] = (df["L2(cm)"] * 101) / df["L1(cm)"]
#--------------------------

# data information after making new columns
print("********** Data After Feature Extraction **********")
print('')
print(df.info())
print('='*50)
print('')
#----------------------------

# plot the results
print("********** Plot The Results **********")
fig, axes = plt.subplots(1, 2, figsize=(8, 8))

x0 = df["T(K)"]
y0 = df["R(ohm)"]
m, b = np.polyfit(x0, y0, 1)
axes[0].scatter(df["T(K)"], df["R(ohm)"], color="blue", label='Raw Data')
axes[0].plot(x0, m*x0+b, color='red', ls='--', label='Fit Line')
axes[0].set_title(r"R($\Omega$) Vs T(K)")
axes[0].text(x0.mean(), m*x0.mean()+b, f"y = {m:.3f}x + {b:.3f}")
axes[0].set_xlabel("T(K)")
axes[0].set_ylabel(r"R($\Omega$)")
axes[0].legend()
axes[0].grid(alpha=0.5, ls='--')

x1 = df["theta(degree)"]
y1 = df["R(ohm)"]
m, b = np.polyfit(x1, y1, 1)
axes[1].scatter(df["theta(degree)"], df["R(ohm)"], color="blue", label='Raw Data')
axes[1].plot(x1, m*x1+b, color='red', ls='--', label='Fit Line')
axes[1].set_title(r"R($\Omega$) Vs T($^\circ C$)")
axes[1].text(x1.mean(), m*x1.mean()+b, f"y = {m:.3f}x + {b:.3f}")
axes[1].set_xlabel(r"T($^\circ C$)")
axes[1].set_ylabel(r"R($\Omega$)")
axes[1].legend()
axes[1].grid(alpha=0.5, ls='--')

plt.tight_layout()
plt.show()

#-----------------------
# df.to_csv(r"C:\Users\Sisto\Documents\Library\FUM\Solid State Az\Session1\Final_Dataset.csv", index=False)
