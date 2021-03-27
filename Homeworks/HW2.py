from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns


Xb,yb =load_boston(return_X_y=True)

df_boston = pd.DataFrame(Xb,columns = load_boston().feature_names)
df_boston.head()
df_boston.info()
df_boston.describe()
df_boston.isna()
df_boston.isna().sum()
df_boston.isnull()
df_boston.isnull().sum()
df_boston.duplicated()
df_boston.duplicated().sum()
sns.pairplot(df_boston)
plt.figure(figsize=(16, 8)) ??
sns.distplot(df_boston)
df_boston.corr()

corr = df_boston.corr()
plt.figure(figsize=(14, 14))
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True, annot = True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
ax.set_ylim(len(corr)+0.5, -0.5);
