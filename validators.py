import re
from typing import Optional

class CryptoValidator:
    def __init__(self):
        # Precompiled regex patterns for performance
        self.address_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
        self.txid_pattern = re.compile(r'^[a-fA-F0-9]{64}$')

    def is_valid_address(self, address: str) -> bool:
        """Validates a Bitcoin address."""
        return bool(self.address_pattern.match(address))

    def is_valid_txid(self, txid: str) -> bool:
        """Validates a Bitcoin transaction ID."""
        return bool(self.txid_pattern.match(txid))

    def validate(self, address: Optional[str] = None, txid: Optional[str] = None) -> bool:
        """Validates both address and transaction ID if provided."""
        if address and not self.is_valid_address(address):
            raise ValueError(f'Invalid Bitcoin address: {address}')
        if txid and not self.is_valid_txid(txid):
            raise ValueError(f'Invalid transaction ID: {txid}')
        return True
