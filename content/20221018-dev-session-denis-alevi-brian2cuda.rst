Dev session: Denis Alevi: Brian2CUDA
###############################################
:date: 2022-10-18 10:38:20
:modified: 2022-10-18 10:38:20
:authors: Ankur Sinha
:category: Events
:tags: Brian2CUDA, Dev session, GPU, Python, C++, CUDA, Nvidia, Simulation, Code generation
:slug: dev-session-denis-alevi-brian2cuda
:summary: `Denis Alevi`_ will introduce the `Brian2CUDA`_ tool in this session, and discuss its development. We will also have a discussion on GPU based simulation in neuroscience after the presentation.

`Denis Alevi`_ will introduce the `Brian2CUDA`_ tool in this session, and discuss its development. We will also have a discussion on GPU based simulation in neuroscience after the presentation.

- Date: Thursday, November 3, 2022, 1600 UTC (Click `here <https://www.timeanddate.com/worldclock/fixedtime.html?msg=Dev+session%3A+Denis+Alevi+Brian2CUDA&iso=20221103T16&p1=136&ah=1>`__ to see your local time).
- Location (Zoom): `Link <https://ucl.zoom.us/j/95692778384?pwd=VldIQ3hPTU1zczNpYjQxSSt4Z25xdz09>`__ (Zoom login required)
- `Click here to download the calendar invite to add this meeting your calendar </extras/ics/20221103-dev-session-denis-alevi-brian2cuda.ics>`__

The abstract for the talk is below:

Graphics processing units (GPUs) are widely available and have been used with
great success to accelerate scientific computing in the last decade. These
advances, however, are often not available to researchers interested in
simulating spiking neural networks, but lacking the technical knowledge to
write the necessary low-level code. Writing low-level code is not necessary
when using the popular Brian simulator, which provides a framework to generate
efficient CPU code from high-level model definitions in Python. Here, we
present Brian2CUDA, an open-source software that extends the Brian simulator
with a GPU backend. Our implementation generates efficient code for the
numerical integration of neuronal states and for the propagation of synaptic
events on GPUs, making use of their massively parallel arithmetic capabilities.
We benchmark the performance improvements of our software for several model
types and find that it can accelerate simulations by up to three orders of
magnitude compared to Brian’s CPU backend. Currently, Brian2CUDA is the only
package that supports Brian’s full feature set on GPUs, including arbitrary
neuron and synapse models, plasticity rules, and heterogeneous delays. When
comparing its performance with Brian2GeNN, another GPU-based backend for the
Brian simulator with fewer features, we find that Brian2CUDA gives comparable
speedups, while being typically slower for small and faster for large networks.
By combining the flexibility of the Brian simulator with the simulation speed
of GPUs, Brian2CUDA enables researchers to efficiently simulate spiking neural
networks with minimal effort and thereby makes the advancements of GPU
computing available to a larger audience of neuroscientists.

References:

- Publication: `Brian2CUDA: flexible and efficient simulation of spiking neural network models on GPUs (Frontiers in Neuroinformatics) <https://www.frontiersin.org/articles/10.3389/fninf.2022.883700/abstract>`__
- Documentation: https://brian2cuda.readthedocs.io/en/latest/
- Source code: https://github.com/brian-team/brian2cuda


.. _Brian2CUDA: https://brian2cuda.readthedocs.io/en/latest/
.. _Denis Alevi: https://www.sprekelerlab.org/denis/
.. _CUDA: https://www.nvidia.com/en-gb/geforce/technologies/cuda/
.. _PyNN: http://neuralensemble.org/PyNN/
.. _OpenCL: https://www.khronos.org/opencl/
