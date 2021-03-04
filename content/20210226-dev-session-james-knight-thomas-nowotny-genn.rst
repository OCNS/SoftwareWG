Dev session: James Knight, Thomas Nowotny: GeNN
###############################################
:date: 2021-02-26 18:33:55
:modified: 2021-03-04 12:08:39
:authors: Ankur Sinha
:category: Events
:tags: GeNN, Dev session, GPU, Python, C++, CUDA, Nvidia, Simulation, Code generation
:slug: dev-session-james-knight-thomas-nowotny-genn
:summary: `James Knight`_ and `Thomas Nowotny`_ will introduce the GeNN_ simulation environment and discuss its development in this dev session.


.. raw:: html

   <center>

.. figure:: {static}/images/20210304-genn.png
    :alt: The GeNN simulator
    :width: 50%
    :class: img-responsive
    :target: http://genn-team.github.io/genn/

.. raw:: html

   </center>
   <br />


`James Knight`_ and `Thomas Nowotny`_ will introduce the GeNN_ simulation environment and discuss its development in this dev session.

- Date: March 9, 2021, 1700 UTC (Click `here <https://www.timeanddate.com/worldclock/fixedtime.html?msg=Dev+session%3A+James+Knight%2CThomas+Nowotny%3A+GeNN&iso=20210309T17&p1=136&ah=1>`__ to see your local time).
- Location (Zoom): https://universityofsussex.zoom.us/j/97956408800?pwd=by9yVnhCZTJlenY0bVI4OEc5QWVFQT09

The abstract for the talk is below:

Large-scale numerical simulations of brain circuit models are important for identifying hypotheses on brain functions and testing their consistency and plausibility.
Similarly, spiking neural networks are also gaining traction in machine learning with the promise that neuromorphic hardware will eventually make them much more energy efficient than classical ANNs.
In this dev session, we will present the GeNN_ (GPU-enhanced Neuronal Networks) framework [1], which aims to facilitate the use of graphics accelerators for computational models of large-scale spiking neuronal networks to address the challenge of efficient simulations.
GeNN_ is an open source library that generates code to accelerate the execution of network simulations on NVIDIA GPUs through a flexible and extensible interface, which does not require in-depth technical knowledge from the users.
GeNN_ was originally developed as a pure C++ and CUDA_ library but, subsequently, we have added a Python interface and OpenCL_ backend.
The Python interface has enabled us to develop a PyNN_ [2] frontend and we are also working on a Keras-inspired frontend for spike-based machine learning [3].

In the session we will briefly cover the history and basic philosophy of GeNN_ and show some simple examples of how it is used and how it works inside.
We will then talk in more depth about its development with a focus on testing for GPU dependent software and some of the further developments such as Brian2GeNN [4].

- [1] https://github.com/genn-team/genn
- [2] https://github.com/genn-team/pynn_genn
- [3] https://github.com/genn-team/ml_genn
- [4] https://github.com/brian-team/brian2genn


.. _GeNN: http://genn-team.github.io/genn/
.. _James Knight: http://www.sussex.ac.uk/profiles/415734
.. _Thomas Nowotny: http://www.sussex.ac.uk/profiles/206151
.. _CUDA: https://www.nvidia.com/en-gb/geforce/technologies/cuda/
.. _PyNN: http://neuralensemble.org/PyNN/
.. _OpenCL: https://www.khronos.org/opencl/
