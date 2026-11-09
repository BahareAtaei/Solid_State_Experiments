# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.signal import find_peaks
#====================================

# import file
df = pd.read_csv(r"https://raw.githubusercontent.com/BahareAtaei/Solid_State_Experiments/refs/heads/main/XRD/Initial_Data.csv")
df_vu = pd.read_csv(r"https://raw.githubusercontent.com/BahareAtaei/Solid_State_Experiments/refs/heads/main/XRD/Initial_Data_VU.csv")
df["N_mean"] = (df["N1"] + df["N2"] + df["N3"]) / 3
df_vu["N_mean"] = (df["N1"] + df["N2"] + df["N3"]) / 3
#===============================================

# plot the results
print(f"********** Mean of Number of Photons VS 2 $\theta$ (VU Data)**********")
x = df["2*theta"].to_numpy()
y = df["N_mean"].to_numpy()

# create smooth curve
x_smooth = np.linspace(x.min(), x.max(), 500)
spline = make_interp_spline(x, y, k=3)
y_smooth = spline(x_smooth)

# find two peaks
peaks, properties = find_peaks(y_smooth)
# the two maximum peaks
top_two = peaks[np.argsort(y_smooth[peaks])[-3::2]]
# sort values
top_two = top_two[np.argsort(x_smooth[top_two])]

# plot the results
plt.scatter(df["2*theta"], df["N_mean"], color='blue', label='Raw Data', s=10)
plt.plot(x_smooth, y_smooth, color='black', lw=1.5, label='Connected Points')
for i in top_two:
    plt.axvline(x=x_smooth[i], color='red', ls='--', lw=1.5, label='Top Peaks')
    plt.text(x_smooth[i], y_smooth[i]/2, f"x = {x_smooth[i]:.4f}")
plt.title(r"Number of Photons VS 2$\theta$ (Experiment Data)")
plt.xlabel(r"2$\theta$")
plt.ylabel("Mean Number of Photons")
plt.legend()
plt.grid(alpha=0.5, ls='--')
plt.tight_layout()
plt.show()
print('='*50)
print('')
#====================================

# plot the vu data
print(f"********** Mean of Number of Photons VS 2 $\theta$ (VU Data)**********")
x_vu = df_vu["2*theta"].to_numpy()
y_vu = df_vu["N_mean"].to_numpy()

# create smooth curve
x_smooth_vu = np.linspace(x_vu.min(), x_vu.max(), 500)
spline_vu = make_interp_spline(x_vu, y_vu, k=3)
y_smooth_vu = spline(x_smooth_vu)

# vertical lines
peaks, properties = find_peaks(y_smooth_vu)
top_two = peaks[np.argsort(y_smooth_vu[peaks])[-3::2]]
top_two = top_two[np.argsort(x_smooth_vu[top_two])]

# plot the results
plt.scatter(df_vu["2*theta"], df_vu["N_mean"], color='blue', s=10, label='Raw Data')
plt.plot(x_smooth_vu, y_smooth_vu, color='black', label='Connected Points')
for i in top_two:
    plt.axvline(x=x_smooth_vu[i], color='red', label='Top Peaks', ls='--', lw=1.5)
    plt.text(x_smooth_vu[i], y_smooth_vu[i]/2, f"x = {x_smooth_vu[i]:.4f}")
plt.title(r"Number of Photons VS 2$\theta$ (VU Data)")
plt.xlabel(r"2$\theta$")
plt.ylabel("Mean Number of Photons")
plt.legend()
plt.grid(alpha=0.5, ls='--')
plt.tight_layout()
plt.show()
print('='*50)
print('')
#==========================================

# df.to_csv(r"C:\Users\Sisto\Documents\Library\FUM\Solid State Az\session2\XRD_final.csv", index=False)
# df_vu.to_csv(r"C:\Users\Sisto\Documents\Library\FUM\Solid State Az\session2\XRD_final_VU.csv", index=False)
