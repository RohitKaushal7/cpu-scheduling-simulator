.. CPU Scheduling Simulator documentation master file, created by
   sphinx-quickstart on Sat Jul  4 08:06:20 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CPU Scheduling Simulator's documentation!
====================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


_
_
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Demo
=======
.. automodule:: src.app
   :members:

.. image:: /images/fcfs.png
    :alt: FCFS
.. image:: /images/sjf.png
    :alt: Shortest Remaining Time First
.. image:: /images/pr-np.png
    :alt: Priority Non-Preemptive
.. image:: /images/pr-p.png
    :alt: Priority Preemptive
.. image:: /images/srtf.png
    :alt: Shortest Remaining Time First
.. image:: /images/round-rbn.png
    :alt: Round Robin

.. image:: /images/comp.png
    :alt: Comparison of Scheduling Algorithms


Process 
===========
.. autoclass:: src.utils.process.Process
   :members:

_

Scheduling Algorithms
======================
All the algorithms expects:
   Args:
         processes (:class:`src.utils.process.Process`):  An array of process to be scheduled.

   Returns:
      Dictionary.  the result of the scheduling::

         {
            'name': 'Algo Name',
            'avg_waiting_time': total_waiting_time/len(proc),
            'avg_response_time': total_response_time/len(proc),
            'avg_turnaround_time': total_turnaround_time/len(proc),
            'processes': proc, # modified scheduled processes
            'gantt': gantt # gantt chart array
         }


Non Preemptive
++++++++++++++
.. automodule:: src.algorithms.fcfs
   :members:
.. automodule:: src.algorithms.sjf
   :members:
.. automodule:: src.algorithms.priority
   :members:

Preemptive
++++++++++++++
.. automodule:: src.algorithms.srtf
   :members:
.. automodule:: src.algorithms.priority_preemptive
   :members:
.. automodule:: src.algorithms.round_robin
   :members:


_

Tables
=======
.. automodule:: src.utils.table
   :members:


_

Graphs
========
Visual representation of Scheduling Algorithms

.. automodule:: src.utils.graph
   :members: