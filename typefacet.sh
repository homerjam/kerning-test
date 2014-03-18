#!/bin/sh

cd typefacet

# help
#env PYTHONPATH=dependencies/RoboFab/lib:dependencies/pystache:dependencies/svgwrite:dependencies/PyYaml/lib:dependencies/FontTools/Lib:python/src-main python python/src-main/autokern/Autokern.py -h

# defaults
	# --ufo-src-path "../nevis-Bold.ufo" \
	# --ufo-dst-path "../nevis-Bold-kerned.ufo" \
	# --min-distance-ems 0.00 \
	# --max-distance-ems 0.00 \
	# --max-x-extrema-overlap-ems 0.0 \
	# --intrusion-tolerance-ems 0.0 \
	# --precision-ems 0.005 \
	# --log-path ../logs \
	# --kern-samples-only

env PYTHONPATH=dependencies/RoboFab/lib:dependencies/pystache:dependencies/svgwrite:dependencies/PyYaml/lib:dependencies/FontTools/Lib:python/src-main python python/src-main/autokern/Autokern.py \
	--ufo-src-path "../nevis-Bold.ufo" \
	--ufo-dst-path "../nevis-Bold-kerned.ufo" \
	--min-distance-ems 0.03 \
	--max-distance-ems 0.09 \
	--max-x-extrema-overlap-ems 0.2 \
	--intrusion-tolerance-ems 0.3 \
	--precision-ems 0.005 \
	--log-path ../logs \
	#--kern-samples-only