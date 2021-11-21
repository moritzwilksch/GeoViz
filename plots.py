#%%
import geopandas as gpd
import matplotlib.pyplot as plt
from numpy import UFUNC_BUFSIZE_DEFAULT
import seaborn as sns

# import matplotlib_inline
# matplotlib_inline.backend_inline.set_matplotlib_formats("png")

BBOX = (-79.0193, 35.9335, -78.7910, 36.0610)


#%%
# Data Loading
streets = gpd.read_file("data/nc/gis_osm_roads_free_1.shp", bbox=BBOX)
water = gpd.read_file("data/nc/gis_osm_waterways_free_1.shp", bbox=BBOX)
nature = gpd.read_file("data/nc/gis_osm_landuse_a_free_1.shp", bbox=BBOX).query(
    "fclass.isin('park forest nature_reserve'.split())"
)
buildings = gpd.read_file("data/nc/gis_osm_buildings_a_free_1.shp", bbox=BBOX)

#%%

fig, ax = plt.subplots(1, 1, figsize=(16, 10))


streets.plot(ax=ax, color="black", linewidth=0.7)
water.plot(ax=ax, color="lightblue", linewidth=2)
nature.plot(ax=ax, color="green", linewidth=1, alpha=0.25)
buildings.plot(ax=ax, color="0.8")

ax.set_xlim(-78.9695, -78.9124)
ax.set_ylim(35.9911, 36.0229)
sns.despine(left=True, bottom=True)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Durham, NC", weight="bold", fontsize=20)
plt.tight_layout()
plt.savefig("durham.png", dpi=300, facecolor="w")
plt.close()
#%%
