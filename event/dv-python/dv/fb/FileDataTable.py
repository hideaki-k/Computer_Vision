# automatically generated by the FlatBuffers compiler, do not modify

# namespace: dv

import flatbuffers


class FileDataTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFileDataTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FileDataTable()
        x.Init(buf, n + offset)
        return x

    # FileDataTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FileDataTable
    def Table(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FileDataDefinition import FileDataDefinition
            obj = FileDataDefinition()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FileDataTable
    def TableLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0


def FileDataTableStart(builder):
    builder.StartObject(1)


def FileDataTableAddTable(builder, Table):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Table), 0)


def FileDataTableStartTableVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def FileDataTableEnd(builder):
    return builder.EndObject()
