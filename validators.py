import re

# Standard regular expressions for crypto address patterns
BTC_ADDRESS_RE = re.compile(r'^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[ac-hj-np-z02-9]{11,71})$')
ETH_ADDRESS_RE = re.compile(r'^0x[a-fA-F0-9]{40}$')
TX_HASH_RE = re.compile(r'^(0x)?[a-fA-F0-9]{64}$')

def validate_symbol(symbol: str) -> bool:
    """Validate if the cryptocurrency symbol is in a standard ticker format."""
    if not symbol or not isinstance(symbol, str):
        return False
    return bool(re.match(r'^[A-Z0-9]{2,10}$', symbol.upper()))

def validate_btc_address(address: str) -> bool:
    """Validate standard Bitcoin address formats (P2PKH, P2SH, Bech32)."""
    if not address or not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_RE.match(address))

def validate_eth_address(address: str) -> bool:
    """Validate standard Ethereum address format."""
    if not address or not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_RE.match(address))

def validate_tx_hash(tx_hash: str) -> bool:
    """Validate common 64-character hex transaction hashes."""
    if not tx_hash or not isinstance(tx_hash, str):
        return False
    return bool(TX_HASH_RE.match(tx_hash))
