#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# import matplotlib_inline
# matplotlib_inline.backend_inline.set_matplotlib_formats("png")

BBOX = (12.8193, 52.3303, 13.2759, 52.5225)


#%%
# Data Loading
streets = gpd.read_file("data/potsdam/gis_osm_roads_free_1.shp", bbox=BBOX)
water = gpd.read_file("data/potsdam/gis_osm_waterways_free_1.shp", bbox=BBOX)
nature = gpd.read_file("data/potsdam/gis_osm_landuse_a_free_1.shp", bbox=BBOX).query(
    "fclass.isin('park forest nature_reserve'.split())"
)
buildings = gpd.read_file("data/potsdam/gis_osm_buildings_a_free_1.shp", bbox=BBOX)

#%%

fig, ax = plt.subplots(1, 1, figsize=(16, 10))

streets.query("fclass.isin(@use_fclasses)").plot(ax=ax, color="black", linewidth=0.7)
water.plot(ax=ax, color="lightblue", linewidth=2)
# nature.plot(ax=ax, color="green", linewidth=1, alpha=0.25)
# buildings.plot(ax=ax, color="0.8")

ax.set_xlim(13, 13.12)
ax.set_ylim(52.38, 52.43)
sns.despine(left=True, bottom=True)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout()
