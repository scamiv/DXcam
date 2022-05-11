import enum


class ProcessorBackends(enum.Enum):
    PIL = 0
    NUMPY = 1


class Processor:
    def __init__(self, backend=ProcessorBackends.NUMPY):
        self.backend = self._initialize_backend(backend)

    def process(self, rect, width, height, region, rotation_angle):
        return self.backend.process(rect, width, height, region, rotation_angle)

    def _initialize_backend(self, backend):
        if backend == ProcessorBackends.NUMPY:
            from .numpy_processor import NumpyProcessor

            return NumpyProcessor()
