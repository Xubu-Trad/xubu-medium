"""Decode the preserved R2 hex and verify its exact inverse. Standard library only."""
from pathlib import Path
from hashlib import sha256

folder = Path(__file__).resolve().parent
C = ''.join((folder / '01-source.hex').read_text(encoding='ascii').split()).lower()
assert len(C) == 2884
assert sha256(C.encode('ascii')).hexdigest() == '18f043170bc47a7d3aa9ee6989fe964803d240c90d62717b7fb7ad16539acd76'

# Rearrange individual hex digits, including the declared two-byte reading rotation.
R = ''.join(C[(320 + 641*j) % len(C)] for j in range(len(C)))
message = bytes.fromhex(R)

# Reconstruct every source digit. No padding, discarded bytes or text corrections.
assert ''.join(R[(4 + 9*j) % len(C)] for j in range(len(C))) == C
assert sha256(message).hexdigest() == '2a77d034354b3ee698dd0266f93dfd5627e033cb8f79ec891498b80b7eab0e52'

(folder / '02-reordered.hex').write_bytes(R.encode('ascii'))
(folder / '03-message.txt').write_bytes(message)
print(message.decode('ascii'), end='')
