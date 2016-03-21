"""
File: cashier.py
Author: Ken Lambert
Editor: Leigh Stauffer
Project 7

Models multiple cashiers.
"""

from arrayqueue import ArrayQueue

class Cashier(object):
    """Represents a cashier."""

    def __init__(self, number):
        """Maintains a cashier number, a queue of customers,
        number of customers served, total customer wait time,
        and a current customer being processed."""
        self._number = number
        self._totalCustomerWaitTime = 0
        self._customersServed = 0
        self._currentCustomer = None
        self._queue = ArrayQueue()

    def addCustomer(self, c):
        """Adds an arriving customer to my line."""
        self._queue.add(c)
   
    def serveCustomers(self, currentTime):
        """Serves my cuatomers during a given unit of time."""
        if self._currentCustomer is None:
            # No customers yet
            if self._queue.isEmpty():
                return
            else:
                # Pop first waiting customer and tally results
                self._currentCustomer = self._queue.pop()
                self._totalCustomerWaitTime += \
                                            currentTime - \
                                            self._currentCustomer.arrivalTime()
                self._customersServed += 1

        # Give a unit of service
        self._currentCustomer.serve()

        # If current customer is finished, send it away   
        if self._currentCustomer.amountOfServiceNeeded() == 0:
            self._currentCustomer = None
   
    def __str__(self):
        """Returns my results: my number, my total customers served,
        my average wait time per customer, and customers left on my queue."""
        if self._customersServed != 0:
            aveWaitTime = float(self._totalCustomerWaitTime) /\
                          self._customersServed
        else:
            aveWaitTime = 0.0
        result = "%4d %8d %13.2f %8d" % (self._number,
                                         self._customersServed,
                                         aveWaitTime,
                                         len(self._queue))
        return result
