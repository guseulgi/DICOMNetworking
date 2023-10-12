from pydicom.uid import ExplicitVRLittleEndian
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import CTImageStorage

debug_logger()

ae = AE()
ae.add_requested_context(CTImageStorage)
assoc = ae.associate("127.0.0.1", 11112)

if assoc.is_established:
    print('Association established with Echo SCP!')
    status = assoc.send_c_echo()
    assoc.release()
else:
    print('Failed to associate')
