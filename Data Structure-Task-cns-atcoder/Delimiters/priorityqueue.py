class priorityqueue:
    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self._qlist)
    def enqueue(self, item, priority):
        entry = PriorityQEntry(item, priority)
        self._qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty(), "cannot dequeue form an empty queue"
        highest = self._qlist[i].priority
        for i in range(self.len()):
            if self._qlist[i].priority <highest:
                highest = self._qlist[i].priority
        entry = self._qlist.pop(highest)
        return entry.item
class PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

