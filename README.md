# GeoViz
Creating beautiful Geo Visualization with geopandas.

<img src="durham.png">



# Reproduce
1. Create & activate virtual environment
```bash
python3 -m venv env
source env/bin/activate
```
2. Install dependencies
```bash
make install
```
3. Download data
Data is downloaded from [geofabrik.de](https://www.geofabrik.de).

```bash
make data/download-nc
```

4. Run script
```bash
python plots.py
```