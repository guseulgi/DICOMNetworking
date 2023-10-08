from pydicom.uid import ExplicitVRLittleEndian
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import CTImageStorage

debug_logger()
ae = AE()
ae.add_supported_context(CTImageStorage, ExplicitVRLittleEndian)
ae.start_server(("127.0.0.1", 11112), block=True)
