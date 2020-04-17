---
author: mommermi
comments: true
date: 2019-02-12 21:29:44+00:00
layout: post
link: https://michaelmommert.wordpress.com/2019/02/12/travis-ci-builds-wont-start/
slug: travis-ci-builds-wont-start
title: Travis-CI builds won't start
wordpress_id: 577
categories:
- software
---

I was having troubles using Travis-CI and github that I would like to spare you: after modifying the `.travis.yml` of my github repository and pushing the changes to an already submitted pull request, the Travis-CI build checks just wouldn't start. It's not that the checks failed, they just simply would not start.

The problem was that this made debugging pretty much impossible, as there was no way of retrieving information on what went wrong. Spending too many hours and about 100 commits to the pull request later, I think I figured out what went wrong:

`.travis.yml` does not like tabs. Using emacs as my python IDE, am used to hitting tab a lot and emacs is smart enough to replace tabs with an equivalent number of white spaces. However, that did not happen in the case of `.travis.yml`- tabs stayed as tabs.

So please watch out and keep in mind that tabs will cause issues here...
