.. VentMapp3r documentation master file, created by
   sphinx-quickstart on Fri Dec 14 15:34:18 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to VentMapp3r's documentation!
==================================

*VentMapp3r* (pronounced ventmapper) is a CNN-based segmentation technique of the ventricular system
using MRI images from BrainLab.
It can deal with brains with extensive atrophy and segments the ventricles in seconds.
It can segment the ICV with either T1-weighted image as the only input, or with different combinations involving a T1, T2, and FLAIR image.

.. image:: images/ventmapper_process.png
    :width: 550px
    :alt: Graph abstract
    :align: center

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   before_install
   install
   beginner
   vent_seg
   issues
   docker

Indices and tables
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
