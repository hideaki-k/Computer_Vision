# automatically generated by the FlatBuffers compiler, do not modify

# namespace: dv

import flatbuffers


class IMU(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsIMU(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = IMU()
        x.Init(buf, n + offset)
        return x

    # IMU
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// Timestamp (µs).
# IMU

    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

# /// Temperature, measured in °C.
# IMU

    def Temperature(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Acceleration in the X axis, measured in g (9.81m/s²).
# IMU

    def AccelerometerX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Acceleration in the Y axis, measured in g (9.81m/s²).
# IMU

    def AccelerometerY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Acceleration in the Z axis, measured in g (9.81m/s²).
# IMU

    def AccelerometerZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Rotation in the X axis, measured in °/s.
# IMU

    def GyroscopeX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Rotation in the Y axis, measured in °/s.
# IMU

    def GyroscopeY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Rotation in the Z axis, measured in °/s.
# IMU

    def GyroscopeZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Magnetometer X axis, measured in µT (magnetic flux density).
# IMU

    def MagnetometerX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Magnetometer Y axis, measured in µT (magnetic flux density).
# IMU

    def MagnetometerY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0


# /// Magnetometer Z axis, measured in µT (magnetic flux density).
# IMU

    def MagnetometerZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0


def IMUStart(builder):
    builder.StartObject(11)


def IMUAddTimestamp(builder, timestamp):
    builder.PrependInt64Slot(0, timestamp, 0)


def IMUAddTemperature(builder, temperature):
    builder.PrependFloat32Slot(1, temperature, 0.0)


def IMUAddAccelerometerX(builder, accelerometerX):
    builder.PrependFloat32Slot(2, accelerometerX, 0.0)


def IMUAddAccelerometerY(builder, accelerometerY):
    builder.PrependFloat32Slot(3, accelerometerY, 0.0)


def IMUAddAccelerometerZ(builder, accelerometerZ):
    builder.PrependFloat32Slot(4, accelerometerZ, 0.0)


def IMUAddGyroscopeX(builder, gyroscopeX):
    builder.PrependFloat32Slot(5, gyroscopeX, 0.0)


def IMUAddGyroscopeY(builder, gyroscopeY):
    builder.PrependFloat32Slot(6, gyroscopeY, 0.0)


def IMUAddGyroscopeZ(builder, gyroscopeZ):
    builder.PrependFloat32Slot(7, gyroscopeZ, 0.0)


def IMUAddMagnetometerX(builder, magnetometerX):
    builder.PrependFloat32Slot(8, magnetometerX, 0.0)


def IMUAddMagnetometerY(builder, magnetometerY):
    builder.PrependFloat32Slot(9, magnetometerY, 0.0)


def IMUAddMagnetometerZ(builder, magnetometerZ):
    builder.PrependFloat32Slot(10, magnetometerZ, 0.0)


def IMUEnd(builder):
    return builder.EndObject()