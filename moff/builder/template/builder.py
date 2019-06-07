
from moff.node import NodeConvertible
from abc import abstractmethod


class Builder (NodeConvertible):

    @abstractmethod
    def add(self, anyone):
        pass

    @abstractmethod
    def is_mergeable(self, builder):
        """

        check instance is mergeable or not.

        Parameters
        ----------
        builder: moff.builder.Builder
          this is the merge input.

        Returns
        -------
        result: bool
          if mergeable return true, otherwise false.
        """

        pass

    @abstractmethod
    def merge(self, builder):
        """

        merge instance and instance then return merged instance.

        Parameters
        ----------
        builder: moff.builder.Builder
          this is the merge input.

        Returns
        -------
        any: moff.builder.Builder
          have not to be new instance.
        """

        pass

    @abstractmethod
    def build_node(self):
        pass

    # override
    def __node__(self):
        return self.build_node()
