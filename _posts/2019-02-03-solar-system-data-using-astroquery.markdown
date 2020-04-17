---
author: mommermi
comments: true
date: 2019-02-03 22:07:54+00:00
layout: post
link: https://michaelmommert.wordpress.com/2019/02/03/solar-system-data-using-astroquery/
slug: solar-system-data-using-astroquery
title: Solar System Data using astroquery
wordpress_id: 552
categories:
- python
- sbpy
- software
---

As mentioned in an [earlier post](https://michaelmommert.wordpress.com/2016/01/08/a-python-module-to-query-jpl-horizons/), I published some code to query the JPL Horizons system, which provides ephemerides, orbital elements, and state vectors for Solar System bodies, in the framework of _astroquery_.

[_astroquery_](https://github.com/astropy/astroquery) is an _[astropy](http://www.astropy.org)_ affiliated package that provides access to a wide range of astronomical data catalogs, archives, and services within Python. Hence, _astroquery_ is the logical place for Solar System-related query functionality.

As part of_ the [sbpy](http://sbpy.org) _project, a number of sub-modules have been added to _astroquery _or extended. Here, I would like to introduce some functionality briefly:


### _[jplhorizons](https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html)_ - JPL Horions Queries


The [JPL Horizons](https://ssd.jpl.nasa.gov/horizons.cgi) service provides ephemerides, state vectors, and orbital elements for every known body in the Solar System - including the [_SpaceX Roadster_](https://en.wikipedia.org/wiki/Elon_Musk%27s_Tesla_Roadster) (object id -143205). If you would like to know where you could see the Roadster in the sky (if you had a telescope large enough) for your location, jplhorizons can provide you exactly that information:

[sourcecode language="python" wraplines="false" collapse="false"]
from astroquery.jplhorizons import Horizons
from astropy.time import Time

# define epoch for query
epoch = Time('2019-02-03 20:09', format='iso')

# define target
# '-143205' is the Horizons-internal id for this object, use&lt;span 				data-mce-type="bookmark" 				id="mce_SELREST_start" 				data-mce-style="overflow:hidden;line-height:0" 				style="overflow:hidden;line-height:0" 			&gt;&lt;/span&gt; id_type='id'
# 'G37' is the IAU code for Lowell's Discovery Channel Telescope
obj = Horizons('-143205', id_type='id', location='G37', epochs=epoch.jd)

# query ephemerides
eph = obj.ephemerides()

print(eph['RA', 'DEC', 'delta', 'V'])
[/sourcecode]

    
       RA       DEC          delta        V
       deg      deg           AU         mag
    --------- -------- ---------------- -----
    338.13194 -8.76581 2.43178151964055 28.98
    


So, the roadster is 2.432 au from Earth with an apparent magnitude of 29.0? We might want to wait for it to come a little bit closer to observe it.

Obtaining orbital elements and state vectors for any object is just as easy. Simply define the target as a _Horizons_ object and then use the corresponding query function. The output is always in the form of an [_astropy_ Table](http://docs.astropy.org/en/stable/table/), supporting [_astropy_ units](http://docs.astropy.org/en/stable/units/).

For more information, have a look at the [documentation](https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html), or contact the [author](https://michaelmommert.wordpress.com/) of _jplhorizons_.


### _[jplsbdb](https://astroquery.readthedocs.io/en/latest/jplsbdb/jplsbdb.html)_ - JPL Small-Body Database Browser Queries


The [JPL Small-Body Database Browser](https://ssd.jpl.nasa.gov/sbdb.cgi) is a query tool that provides pretty much all available data on a Solar System small-body that is available on the JPL servers.

_jplsbdb_ is easy to use:

[sourcecode language="python" wraplines="false" collapse="false"]
from astroquery.jplsbdb import SBDB
SBDB.query('3552')
[/sourcecode]

    
    OrderedDict([('object', OrderedDict([('shortname', '3552 Don Quixote'), ('neo', True), ('orbit_class', OrderedDict([('name', 'Amor'), ('code', 'AMO')])), ('pha', False), ('spkid', '2003552'), ('kind', 'an'), ('orbit_id', '188'), ('fullname', '3552 Don Quixote (1983 SA)'), ('des', '3552'), ('prefix', None)])), ('signature', OrderedDict([('source', 'NASA/JPL Small-Body Database (SBDB) API'), ('version', '1.0')])), ('orbit', OrderedDict([('source', 'JPL'), ('cov_epoch', Unit("2.45657e+06 d")), ('moid_jup', Unit("0.441 AU")), ('t_jup', '2.315'), ('condition_code', '0'), ('not_valid_before', None), ('rms', '0.51'), ('model_pars', []), ('orbit_id', '188'), ('producer', 'Otto Matic'), ('first_obs', '1983-09-10'), ('soln_date', '2018-07-06 06:55:08'), ('two_body', None), ('epoch', Unit("2.4582e+06 d")), ('elements', OrderedDict([('e', '0.709'), ('e_sig', '4.8e-08'), ('a', Unit("4.26 AU")), ('a_sig', Unit("2.3e-08 AU")), ('q', Unit("1.24 AU")), ('q_sig', Unit("2e-07 AU")), ('i', Unit("31.1 deg")), ('i_sig', Unit("1.1e-05 deg")), ('om', Unit("350 deg")), ('om_sig', Unit("1e-05 deg")), ('w', Unit("316 deg")), ('w_sig', Unit("1.1e-05 deg")), ('ma', Unit("355 deg")), ('ma_sig', Unit("3.9e-06 deg")), ('tp', Unit("2.45825e+06 d")), ('tp_sig', Unit("3.5e-05 d")), ('per', Unit("3210 d")), ('per_sig', Unit("2.6e-05 d")), ('n', Unit("0.112 deg / d")), ('n_sig', Unit("9.2e-10 deg / d")), ('ad', Unit("7.27 AU")), ('ad_sig', Unit("4e-08 AU"))])), ('equinox', 'J2000'), ('data_arc', '12717'), ('not_valid_after', None), ('n_del_obs_used', None), ('sb_used', 'SB431-N16'), ('n_obs_used', '869'), ('comment', None), ('pe_used', 'DE431'), ('last_obs', '2018-07-05'), ('moid', Unit("0.334 AU")), ('n_dop_obs_used', None)]))])
    


The default query returns a lot of information - even more is available upon request. The output is provided in the form of an OrderedDict in a tree-like structure.

In order to get a better overview of the data available, _jplsbdb_ provides a function to print the query information as a schematic:

[sourcecode language="python" wraplines="false" collapse="false"]
from astroquery.jplsbdb import SBDB
data = SBDB.query('3552')
print(SBDB.schematic(data))
[/sourcecode]

    
    +-+ object:
    | +-- shortname: 3552 Don Quixote
    | +-- neo: True
    | +-+ orbit_class:
    | | +-- name: Amor
    | | +-- code: AMO
    | +-- pha: False
    | +-- spkid: 2003552
    | +-- kind: an
    | +-- orbit_id: 188
    | +-- fullname: 3552 Don Quixote (1983 SA)
    | +-- des: 3552
    | +-- prefix: None
    +-+ signature:
    | +-- source: NASA/JPL Small-Body Database (SBDB) API
    | +-- version: 1.0
    ...


For more information, have a look at the [documentation](https://astroquery.readthedocs.io/en/latest/jplsbdb/jplsbdb.html), or contact the [author](https://michaelmommert.wordpress.com/) of _jplhorizons_.


### _[jplspec](https://astroquery.readthedocs.io/en/latest/jplspec/jplspec.html)_ - JPL Molecular Spectroscopy Catalog Queries


The [JPL Molecular Spectroscopy Catalog](https://spec.jpl.nasa.gov/home.html) provides spectroscopic information on a wide range of molecules. For a query example and additional information, I refer to the [jplspec documentation](https://astroquery.readthedocs.io/en/latest/jplspec/jplspec.html).


### _[mpc](https://astroquery.readthedocs.io/en/latest/mpc/mpc.html)_ - Minor Planet Center Ephemerides Queries


The [Minor Planet Center](https://minorplanetcenter.net/) is the official clearing house for all asteroid and comet observations. and provides a number of services and data sets for researchers. The _astroquery_ submodule _mpc_ includes functionality to query ephemerides, orbital elements, registered observatory locations, and observations reported to the MPC. For a full introduction on the provided services, I refer to the [_mpc_ documentation](https://astroquery.readthedocs.io/en/latest/mpc/mpc.html). Here, I simply present a short example for how to query the current ephemerides for asteroid Ceres as seen from the Discovery Channel Telescope (G37):

[sourcecode language="python" wraplines="false" collapse="false"]</pre>
from astroquery.mpc import MPC

eph = MPC.get_ephemeris('Ceres', location='G37', number=1)
print(eph['Date', 'RA', 'Dec'])
[/sourcecode]

    
              Date                  RA                 Dec        
                                   deg                 deg        
    ----------------------- ------------------ -------------------
    2019-02-03 21:57:08.000 241.90666666666667 -14.536111111111111




### skybot - Searching for Solar System bodies in a region of the sky


Coming soon...
