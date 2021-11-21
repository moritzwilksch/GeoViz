data/download-nc:
	wget -O data/nc.shp.zip http://download.geofabrik.de/north-america/us/north-carolina-latest-free.shp.zip 

data/download-potsdam:
	wget -O data/potsdam/brb.shp.zip https://download.geofabrik.de/europe/germany/brandenburg-latest-free.shp.zip 

install:
	pip install --upgrade pip \
	&& pip install -r requirements.txt