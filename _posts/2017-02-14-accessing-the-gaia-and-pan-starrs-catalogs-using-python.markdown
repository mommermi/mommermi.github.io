---
author: mommermi
date: 2017-02-14 05:00:53+00:00
layout: post
title: Accessing the Gaia and Pan-STARRS catalogs using Python
description: |
  This recipe shows how to query the Gaia and Pan-STARRS catalogs using
  astroquery.
categories:
- astronomy
tags:
- open-source software
- note
---

_update 2019/01: I updated the following code to reflect recent developments (mostly the availability of Pan-STARRS in Vizier)_

The recently available [Gaia](http://gaia.esac.esa.int/documentation/GDR1/index.html) and [Pan-STARRS](http://panstarrs.stsci.edu/) data releases are certainly interesting to the majority of astronomers for various reasons. If only there was a way to load the catalog data into Python...


## Gaia catalog access using astroquery.vizier


The Gaia DR1 catalog is accessible through [Vizier](http://vizier.u-strasbg.fr/viz-bin/VizieR), which in turn can be accessed using the [astroquery.vizier](http://astroquery.readthedocs.io/en/latest/vizier/vizier.html) module, providing a comfortable [astropy.table](http://docs.astropy.org/en/stable/table/) output. A simple query could look like this:

```python    
from astroquery.vizier import Vizier 
import astropy.units as u 
import astropy.coordinates as coord

def gaia_query(ra_deg, dec_deg, rad_deg, maxmag=20, 
               maxsources=10000): 
    """
    Query Gaia DR1 @ VizieR using astroquery.vizier
    :param ra_deg: RA in degrees
    :param dec_deg: Declination in degrees
    :param rad_deg: field radius in degrees
    :param maxmag: upper limit G magnitude (optional)
    :param maxsources: maximum number of sources
    :return: astropy.table object
    """
    vquery = Vizier(columns=['Source', 'RA_ICRS', 'DE_ICRS', 
                             'phot_g_mean_mag'], 
                    column_filters={"phot_g_mean_mag": 
                                    ("<%f" % maxmag)}, 
                    row_limit = maxsources) 
 
    field = coord.SkyCoord(ra=ra_deg, dec=dec_deg, 
                           unit=(u.deg, u.deg), 
                           frame='icrs')
    return vquery.query_region(field, 
                               width=("%fd" % rad_deg), 
                               catalog="I/337/gaia")[0] 

# Example query
print(gaia_query(12.345, 67.89, 0.1))
````

Other columns are available, too. Simply add their names as provided [here](http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=I/337/gaia&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa) to the 'columns' list. Also, note that Gaia DR2 has been available since April 2018. In order to query that catalog, simply replace _catalog="I/337/gaia"_ in _vquery.query_region_ with

```python    
catalog="I/345/gaia2"
```

## Pan-STARRS DR1 catalog access


The Pan-STARRS DR1 catalog<del> resides at [MAST](http://archive.stsci.edu/), which unfortunately does not yet have an astroquery interface </del>is now available on Vizier, so we can use pretty much the same code as above:

```python    
from astroquery.vizier import Vizier
import astropy.units as u
import astropy.coordinates as coord

def panstarrs_query(ra_deg, dec_deg, rad_deg, maxmag=20,
                    maxsources=10000):
    """
    Query PanSTARRS @ VizieR using astroquery.vizier
    :param ra_deg: RA in degrees
    :param dec_deg: Declination in degrees
    :param rad_deg: field radius in degrees
    :param maxmag: upper limit G magnitude (optional)
    :param maxsources: maximum number of sources
    :return: astropy.table object
    """
    vquery = Vizier(columns=['objID', 'RAJ2000', 'DEJ2000',
                             'e_RAJ2000', 'e_DEJ2000',
                             'gmag', 'e_gmag',
                             'rmag', 'e_rmag',
                             'imag', 'e_imag',
                             'zmag', 'e_zmag',
                             'ymag', 'e_ymag'],
                    column_filters={"gmag":
                                    ("<%f" % maxmag)},
                    row_limit=maxsources)

    field = coord.SkyCoord(ra=ra_deg, dec=dec_deg,
                           unit=(u.deg, u.deg),
                           frame='icrs')
    return vquery.query_region(field,
                               width=("%fd" % rad_deg),
                               catalog="II/349/ps1")[0]


# Example query
print(panstarrs_query(12.345, 67.89, 0.1))
```

The Vizier query is preferred over the MAST query shown here previously as it is not affected by the field radius limit imposed by the latter.
